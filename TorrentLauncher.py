'''
Created on 2013-04-10

@author: JordSti
'''

import os
import shutil

class TorrentLauncher:
    
    def __init__(self, settings):
        self.client = settings.client
        
        if self.client == "rtorrent":
            self.launcher = rTorrentHandler(settings.torrentFolder)
            
        if self.client == "utorrent":
            self.launcher = uTorrentHandler(settings.clientPath, settings.downloadPath)
        
    
class rTorrentHandler:
    def __init__(self, watchfolder = "watch"):
        self.watchfolder = watchfolder
        
    def launch(self, torrentpath):
        dest = os.path.join(self.watchfolder, os.path.basename(torrentpath))
        shutil.copy(torrentpath, dest)
    
    
class uTorrentHandler:
    
    def __init__(self, path = "", downloadpath = ""):
        self.executable = "uTorrent.exe"
        self.path = path
        self.default_paths = []
        self.default_paths.append("C:\Program Files (x86)\uTorrent")
        self.default_paths.append("C:\Program Files\uTorrent")
        self.default_paths.append(os.path.join(os.environ["APPDATA"],"uTorrent"))
        
        self.downloadpath = downloadpath
        
        if len(path) == 0:
            #search for utorrent
            print "No uTorrent path specified, searching..."
            for p in self.default_paths:
                if os.path.exists(os.path.join(p, self.executable)):
                    self.path = os.path.join(p, self.executable)
                    print "Found at : %s" % (self.path)
                    break
            if len(self.path) == 0:
                print "uTorrent not found !"
    
    def launch(self, torrentpath):

        if not os.path.isabs(torrentpath):
            torrentpath = os.path.abspath(torrentpath)
        
        cmd = self.path + ' /DIRECTORY "%s" "%s"' % (self.downloadpath, torrentpath)
        
        print cmd
        os.system(cmd)