'''
Created on 2013-02-04

@author: JordSti
'''

class WatcherSetting:
    
    def __init__(self):
        self.username = 'username'
        #self.tmpFolder = '/home/rtorrent/tmp'
        #self.torrentFolder = '/home/rtorrent/watch'
        
        self.reloadRules = True
        self.sleepTime = 60*5 #in seconds
        self.tmpFolder = 'tmp'
        
        self.downloadUrl = 'http://www.scenetime.com/download.php/'
        self.rssUrl = 'http://www.scenetime.com/get_rss.php?cat=9,63,43,77,2'

        self.passkey = '00000000000000000000000000000000'
        #bit-torrent client
        #utorrent section
        #self.client = "utorrent"
        #self.clientPath = ""
        #self.downloadPath = "C:\\DownloadTorrent\\"
        #rtorrent section
        self.client = "rtorrent" 
        self.torrentFolder = 'watch'