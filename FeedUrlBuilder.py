'''
Created on 2013-02-05

@author: JordSti
'''


class FeedUrlBuilder:
    
    def __init__(self, rssUrl, username, passkey):
        
        self.username = username
        self.passkey = passkey
        self.rssUrl = rssUrl
        
    def buildUrl(self):
        
        url = self.rssUrl + "&user=" + self.username + "&passkey=" + self.passkey
        
        return url