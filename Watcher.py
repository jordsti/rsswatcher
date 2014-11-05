'''
Created on 2013-02-04

@author: JordSti
'''

import TorrentWatcher
import sys

def printHelp():
    print "Torrent Watcher Help"
    print "python Watcher.py [args]"
    print "-d or debug : start TorrentWatcher in Debug Mode"
    print "-h or help : show this message"
    print "configuration is in WatcherSetting.py"
    print "----------------------------------------------"
    print "if you have some questions you can write to "
    print "jord@sticode.com"
    sys.exit()

if __name__ == '__main__':
    #main here !
    
    #variables
    RunMode = TorrentWatcher.DEFAULT
    
    
    #arguments check
    
    for arg in sys.argv:
        
        if arg == 'debug':
            RunMode = TorrentWatcher.DEBUG
        elif arg == '-d':
            RunMode = TorrentWatcher.DEBUG
        elif arg == '-h':
            printHelp()
        elif arg == 'help':
            printHelp()

    print "---------------------------------------------"
    print "Torrent Watcher For SceneTime"
    print "Developped by JordSti (jord@sticode.com)"
    print "Version 0.0.1"
    print "---------------------------------------------"
    
    watcher = TorrentWatcher.TorrentWatcher(RunMode)
    watcher.initFolder()
    
    watcher.loadFiles()
    #watcher.fetchRss()
    
    #watcher.authenticate()
    
    watcher.watchLoop()