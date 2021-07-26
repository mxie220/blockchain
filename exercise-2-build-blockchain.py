'''
Exercise 2: Constructing and verifying a blockchain.
Author: Michelle Xie
'''
class block:

    def __init__(self):
        self.hash = None
        self.previousBlock = None
        self.nextBlock = None
        self.minerId = None

    def setHash(self, hash):
        self.hash = hash
    
    def getHash(self):
        return self.hash

    def getPreviousBlock(self):
        return self.previousBlock
    
    def setPreviousBlock(self, previousBlock):
        self.previousBlock = previousBlock

    def getNextBlock(self):
        return self.nextBlock
    
    def setNextBlock(self, nextBlock):
        self.nextBlock = nextBlock

    def setMinerId(self, minerId):
        self.minerId = minerId
    

class nounce:

    

class blockchain:

    def __init__(self):
        self.chain = []

    def buildABlockchain(self, numberOfBlocks):
        genesisBlock = block().setMinerId(0)
        

    def mineTheNextBlock(self, currentBlock):
        