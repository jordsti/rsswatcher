'''
Created on 2013-02-04

@author: JordSti
'''

import RulesFile
import RssWatcher
import TorrentHistory
import os
import urllib2
import shutil
import time
import WatcherSetting
import FeedUrlBuilder
import TorrentUrlBuilder
import TorrentLauncher
import Logger

DEFAULT = 0
DEBUG = 1

class TorrentWatcher:
    
    def __init__(self, runMode = DEFAULT, rulesPath = 'rules.txt'):
        
        self.runMode = runMode
        self.settings = WatcherSetting.WatcherSetting()
        
        builder = FeedUrlBuilder.FeedUrlBuilder(self.settings.rssUrl, self.settings.username, self.settings.passkey)
        
        self.rssUrl = builder.buildUrl()
        self.tmpFolder = self.settings.tmpFolder
        #self.torrentFolder = self.settings.torrentFolder
        self.rulesPath = rulesPath
        self.downloadUrl = self.settings.downloadUrl
        self.sleepTime = self.settings.sleepTime
        self.count = 0
        self.log = Logger.LogFile()
        
        launcher = TorrentLauncher.TorrentLauncher(self.settings)
        
        self.launcher = launcher.launcher
        
    #def authenticate(self):
        #removing this
        #auth = SceneTimeAuth.SceneTimeAuth()
        #self.urlOpener = auth.authenticate(self.settings.username, self.settings.password)
    
    
    def initFolder(self):
        
        if not os.path.exists(self.tmpFolder):
            os.mkdir(self.tmpFolder)
            
        #if not os.path.exists(self.torrentFolder):
            #os.mkdir(self.torrentFolder)
    
    def loadFiles(self):
        
        self.rules = RulesFile.RulesFile(self.rulesPath)
        self.log.write('Rules Loaded')
        
        if self.runMode == DEBUG:
            self.printRules()
        
        self.history = TorrentHistory.TorrentHistory()
        self.history.load()
        self.log.write('History Loaded')
        
        if self.runMode == DEBUG:
            self.printHistory()
    
    def printHistory(self):
        
        print "Torrent History :"
        
        for h in self.history.ids:
            print h
        
        print "end Torrent History"
    
    def printRules(self):
        
        print "Rules :"
        for rule in self.rules.rules:
            print rule
            
        print "end Rules"
        
    def fetchRss(self):
        self.rss = RssWatcher.RssWatcher(self.rssUrl)
        self.rss.fetchRss()
        self.rss.parseXml()
        
        self.log.write('Rss Fetched')
        
        
    def getTorrent(self, torrent):
        
        print torrent.link
        
        torrentFile = torrent.getLinkTitle()
        #url = self.downloadUrl + str(torrent.id) + '/' + torrentFile
        
        builder = TorrentUrlBuilder.TorrentUrlBuilder(torrent, self.settings.passkey)
        
        url = builder.buildUrl()
        print url
        localPath = os.path.join(self.tmpFolder,torrentFile)
        #dest = os.path.join(self.torrentFolder,torrentFile)
        
        
        g = urllib2.urlopen(url).read()
        
        #g = self.urlOpener.open(request).read()
        
        f = open(localPath, "wb")
        f.write(g)
        
        f.close()
        
        self.launcher.launch(localPath)
        #shutil.copy(localPath, dest)
    
    def watchTorrents(self):
        
        for torrent in self.rss.torrents:
            
            for rule in self.rules.rules:
                
                if torrent.match(rule):
                    
                    if not self.history.contains(torrent.id):
                        
                        print torrent.title
                        
                        self.getTorrent(torrent)
                        
                        self.history.add(torrent.id)
                        self.history.save()
    
    def watchLoop(self):
        
        while True:
            
            if self.settings.reloadRules:
                #reloading rules
                self.log.write("Rules reloaded")
                self.rules = RulesFile.RulesFile(self.rulesPath)
            
            self.fetchRss()
            
            self.watchTorrents()
            
            self.count = self.count + 1
            self.log.write("Check #"+str(self.count)+ ", done !")
            self.log.write("Going to sleep...")
            time.sleep(self.sleepTime)
    