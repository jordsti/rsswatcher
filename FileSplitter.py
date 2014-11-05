'''
Created on 2013-02-06

@author: JordSti
'''
import hashlib
import os.path
import pickle
import sys
        
def loadSplitFile(filename):
    f = open(filename, 'r')
    p = pickle.Unpickler(f)
    obj = p.load()
    f.close()
        
    return obj

class FileBlock:
    def __init__(self, size, fhash, name):
        self.size = size
        self.fhash = fhash
        self.name = name

class FileSplitter:
    
    def __init__(self, filename, blockSize = 1024*1024*32):
        self.blockinfo = []
        self.filename = filename
        self.size = os.path.getsize(filename)
        self.name = os.path.basename(filename)
        self.blockSize = blockSize
    
    def merge(self, containingFolder, deleteBlocks = False):
        
        tmpfile = os.path.join(containingFolder, '.' + self.name + '.merging')
        
        fmerge = open(tmpfile, 'wb')
        
        for b in enumerate(self.blockinfo):
            bpath = os.path.join(containingFolder, b[1].name)
            if os.path.exists(bpath):
                fblock = open(bpath, 'rb')
                data = fblock.read(self.blockSize)
                cf = self.hashData(data)
                
                if cf == b[1].fhash:
                    fmerge.write(data)
                    fblock.close()
                else:
                    print 'Block: #' + str(b[0]) + ' is corrupted !'
                    print 'Merge abort'
                    break
            
            else:
                print bpath + ' not found !'
                print 'Merge abort...'
                break
        
        #renaming files
        fmerge.close()
        finalfile = os.path.join(containingFolder, self.name)
        i = 0
        while os.path.exists(finalfile):
            finalfile = os.path.join(containingFolder, self.name + '.' + str(i))
            i = i + 1
        
        os.rename(tmpfile, finalfile)
        print 'Merge output: '+ finalfile
    
    def split(self):
        path = os.path.dirname(self.filename)
        
        f = open(self.filename, 'rb')
        
        i = f.read(self.blockSize)
        blockId = 0
        
        while not len(i) == 0:
            blockname = self.name + '.s'+str(blockId)
            newfile = os.path.join(path, blockname)
            fout = open(newfile, 'wb') 
            
            fout.write(i)
            
            fout.close()
            
            hash = self.hashFile(newfile)
            b = FileBlock(len(i), hash, blockname)
            self.blockinfo.append(b)
            
            blockId = blockId + 1
            i = f.read(self.blockSize)
            
            
        f.close()
        
        self.save(filename + '.split')
    
    def hashData(self, data):
        
        hasher = hashlib.md5()
        
        hasher.update(data)
        
        return hasher.hexdigest()
    
    def hashFile(self, path, bufferSize = 1024):
        fcs = open(path, 'rb')
        
        hasher = hashlib.md5()
        
        data = fcs.read(bufferSize)
        
        while len(data) > 0:
            hasher.update(data)
            data = fcs.read(bufferSize)
        
        fcs.close()
        
        return hasher.hexdigest()
    
    def printInfo(self):
        
        print self.filename
        print self.path
        print self.size
        
        for i in enumerate(self.blockinfo):
            print i[1].fhash
            print i[1].size
            print i[1].name
    
    def save(self, destination):
        f = open(destination, 'w')
        
        p = pickle.Pickler(f)
        
        p.dump(self)
        
        f.close()

if __name__ == '__main__':
    print 'FileSplitter v0.0.1'
    print 'Author: JordSti (jord@sticode.com)'
    print '----------------------------------'
    blockSize = 1024*1024*32
    filename = ''
    split = False
    merge = False
    
    
    
    if len(sys.argv) <= 1:
        print 'No argument...'
        #show help
    else:
        for i in enumerate(sys.argv, 1):
            if i[1] == '-s':
                split = True
            elif i[1] == '-m':
                merge = True
            elif i[1] == '-b':
                if len(sys.argv) > i[0] + 1:
                    blockSize = int(sys.argv[i[0]])
            elif i[1] == '-kb':
                if len(sys.argv) > i[0] + 1:
                    blockSize = int(sys.argv[i[0]])*1024
            elif i[1] == '-mb':
                if len(sys.argv) > i[0] + 1:
                    blockSize = int(sys.argv[i[0]])*1024*1024

        #filename must be the last arguments
        filename = sys.argv.pop()
    
    print filename
    
    if os.path.exists(filename):
        if split and merge:
            'Split and merge! You\'re a strange person'
        elif split:
            print 'Splitting File: ' + filename
            print 'Into block of ' + str(blockSize) + ' Byte(s)'
            fs = FileSplitter(filename, blockSize)
            fs.split()
            print 'File splitted !'
        elif merge:
            print 'Merging File: ' + filename
            fs = loadSplitFile(filename)
            print 'Metadata loaded, merging...'
            fs.merge(os.path.dirname(filename))
            
