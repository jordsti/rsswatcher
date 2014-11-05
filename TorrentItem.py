'''
Created on 2013-02-04

@author: JordSti
'''

import re

class TorrentItem:
    
    def __init__(self, title, link, id):
        self.title = title
        self.link = link
        self.id = id
        
    def printData(self):
        print 'Torrent Item'
        print self.title
        print self.id
        print self.link
        
    def getLinkTitle(self):
        return self.title.replace(' ','.') + ".torrent"
        
    def match(self, rules):
        
        p = re.compile(rules)
        
        m = p.match(self.title)
        
        if m:
            return True
        else:
            return False
        
        
