'''
Exercise 2: Block
Author: Michelle Xie
'''
import nounce

class block:

    def __init__(self, value, length):
        self.hash = None
        self.minerId = None
        self.nounce = nounce.nounce().getNounceValue(value, length)

    def setHash(self, hash):
        self.hash = hash
    
    def getHash(self):
        return self.hash

    def setMinerId(self, minerId):
        self.minerId = minerId

    def getMinerId(self):
        return self.minerId

    def getNounce(self):
        return self.nounce