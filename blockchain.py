'''
Exercise 2: Constructing and verifying a blockchain.
Author: Michelle Xie
'''

import block, hashlib

class blockchain:

    def __init__(self, value, length):
        self.chain = []
        self.value = value
        self.length = length

    def build(self, numberOfBlocks):
        print("\nBuilding a blockchain with {0} blocks\n".format(numberOfBlocks))
        minerId = 0
        self.currentBlock = block.block(self.value, self.length) 
        self.currentBlock.setMinerId(minerId)
        self.chain.append({"nounce": self.currentBlock.getNounce(), "miner": self.currentBlock.getMinerId()})

        for num in range(1, numberOfBlocks):
            print("Mining block: {0}\n".format(num))
            self.currentBlock = self.mineTheNextBlock(self.currentBlock)
            self.currentBlock.setMinerId(minerId)
            self.chain.append({"nounce": self.currentBlock.getNounce(), "miner": self.getMinerId()})
        
        print("\nBuild completed.\n")
        return self.chain

    def mineTheNextBlock(self, currentBlock):
        value = str(currentBlock.getHash()) + str(currentBlock.getMinerId())
        nextBlock = block.block(value, self.length)
        text = currentBlock.getHash() + nextBlock.getMinerId() + nextBlock.getNounce()
        hashValue = hashlib.sha256(str.encode(text)).hexdigest()
        nextBlock.setHash(hashValue)
        return nextBlock

    def verifyChain(self, blockchain):
        
        return None

def main():
    numberOfBlocks = 10
    blockchain("0", numberOfBlocks)

main()