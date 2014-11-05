'''
Created on 2013-02-04

@author: JordSti
'''

class RulesFile:
    
    
    def __init__(self, filename):
        self.filename = filename
        self.rules = []
        f = open(filename, 'r')
   
        for line in f:
            rule = line.rstrip('\r\n')
            if not rule.startswith('#'):
                if len(rule) > 0:
                    rule = rule.replace('(SE)','S[0-9]{2}E[0-9]{2}')
                    self.rules.append(rule)

        f.close()
        