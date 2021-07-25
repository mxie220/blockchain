'''
Exercise 2: Constructing and verifying a blockchain.
Author: Michelle Xie
'''
class block:

    def __init__(self):
        __self.hash = None
        __self.previousBlock = None
        __self.nextBlock = None

    def setHash(self, hash):
        __self.hash = hash
    
    def getHash(self):
        return self.hash

    def getPreviousBlock(self):
        return self.previousBlock
    
    def setPreviousBlock(self, previousBlock):
        __self.previousBlock = previousBlock

    def getNextBlock(self):
        return self.nextBlock
    
    def setNextBlock(self, nextBlock):
        __self.previousBlock = nextBlock
    

class blockchain:

    def __init__(self):
        self.chain = []

    def mineTheNextBlock(self, )