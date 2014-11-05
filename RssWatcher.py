'''
Created on 2013-02-04

@author: JordSti
'''

import urllib2
from xml.dom.minidom import parseString
import re
import TorrentItem
import RulesFile

class RssWatcher:
    
    def __init__(self, rssUrl):
        
        self.rssUrl = rssUrl
        self.torrents = []
        self.xmlAvailable = False
        
    def fetchRss(self):
        try:
            f = urllib2.urlopen(self.rssUrl)
        
            self.xmlRss = f.read()
        
            f.close()
            self.xmlAvailable = True
        except:
            print "Request time out !"
            self.xmlRss = ""
        
    def parseXml(self):
        
        if self.xmlAvailable:
            dom = parseString(self.xmlRss)
        
            self.items = dom.getElementsByTagName('item')
        
            for i in enumerate(self.items):
                title = self.getText(i[1], 'title')
                link = self.getText(i[1], 'link')
            
                id = self.parseId(link)
            
                torrent = TorrentItem.TorrentItem(title,link,id)
            
                self.torrents.append(torrent)
        else:
            print "Unable to parse, xml feed wasn't downloaded..."
            
            
    def getText(self, node, tagname):
        
        textnode = node.getElementsByTagName(tagname)[0].childNodes[0]
        
        return textnode.data

    def parseId(self, link):
        regex = '^.+id=([0-9]+)$'
        
        p = re.compile(regex)
        
        m = p.match(link)
        
        return m.group(1)
        


