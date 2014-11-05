'''
Created on 2013-02-05

@author: JordSti
'''

class CategoryCollection:
    
    def __init__(self):
        self.cats = TorrentCategories()
        self.items = []
        
    def count(self):
        return len(self.items)
    
    def addCategoryId(self, id):
        
        if self.cats.containsId(id):
            self.items.append(id)
    
    def getIdList(self):
        
        ids = ''
        
        for i in enumerate(self.items):
            ids = ids + ','
            
        return ids.lstrip(',')

class TorrentCategories:
    
    def __init__(self):
        
        self.categories = { 
                           'Movies/XviD' : 1,
                           'Movies/DVD-R' : 3,
                           'Movie/Packs' : 47,
                           'Movies/Anime' : 56,
                           'Movies/480p' : 57,
                           'Movies/HD' : 59,
                           'Movies/Classic' : 61,
                           'Movies/3D' : 64,
                           'TV/XviD' : 2,
                           'TV/Packs' : 43,
                           'TV/Classic' : 9,
                           'TV-HD' : 63,
                           'TV/SD' : 77,
                           'Games/PC ISO' : 6,
                           'Games/XBOX' : 48,
                           'Games/PS3' : 50,
                           'Games/PSP' : 49,
                           'Games/Wii' : 51,
                           'Games/Nintendo DS' : 55
                           }
        
    def GetText(self, id):
        for i in self.categories.iterkeys():
            
            if self.categories[i] == id:
                return i
        return ''       
    
    
    def containsId(self, id):
        
        for i in self.categories.itervalues():
            
            if i == id:
                return True;
        return False

