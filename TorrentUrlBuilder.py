'''
Created on 2013-02-05

@author: JordSti
'''



class TorrentUrlBuilder:
    
    def __init__(self, torrent, passkey):
        self.torrent = torrent
        self.passkey = passkey
        
        
    def buildUrl(self):
        
        url = "http://www.scenetime.com/download.php/" + str(self.torrent.id) + "/" + self.torrent.getLinkTitle() + "?torrent_pass=" + self.passkey
        
        return url