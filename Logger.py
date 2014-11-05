'''
Created on 2013-05-09

@author: JordSti
'''
import datetime

class LogFile:
    
    def __init__(self, path = "log.txt"):
        
        self.path = path
    
    def write(self, message):
        
        dt = datetime.datetime.now()
        
        fp = open(self.path, 'a+')
        
        line = '%04i/%02i/%02i %02i:%02i:%02i - %s\n' % (dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, message)
        
        print line.rstrip('\n')
        
        fp.write(line)
        
        fp.close()
        