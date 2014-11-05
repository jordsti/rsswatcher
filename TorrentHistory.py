'''
Created on 2013-02-04

@author: JordSti
'''
import os

class TorrentHistory:
    
    def __init__(self):
        
        self.filename = ".history.th"
        
        self.ids = []
        
    
    def add(self, id):
        
        if self.ids.count(str(id)) == 0:
            self.ids.append(str(id))
    
    def contains(self, id):
        
        if self.ids.count(str(id)) == 0:
            return False
        else:
            return True
    
    def save(self):
        
        f = open(self.filename, 'w')
        
        for id in self.ids:
            
            f.write( str(id) + '\n' )
        
        f.close()
    
    def load(self):
        
        if os.path.exists(self.filename):
        
            f = open(self.filename, 'r')
            
            for line in f:
                
                id = line.rstrip('\r\n')
                
                self.ids.append(id)
                
            f.close()