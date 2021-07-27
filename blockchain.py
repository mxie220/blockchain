'''
Exercise 2: Constructing and verifying a blockchain.
Author: Michelle Xie
'''

import block, hashlib

class blockchain:

    def __init__(self, value, length):
        self.chain = []
        self.currentBlock = block.block(value, length) 
        self.currentBlock.setMinerId(0)
        self.chain.append({"nounce": self.currentBlock.getNounce(), "miner": self.currentBlock.getMinerId()})

    def build(self, numberOfBlocks):
        for num in range(1, numberOfBlocks):
            self.currentBlock = self.mineTheNextBlock(self.currentBlock)
            self.chain.append({"nounce": self.currentBlock.getNounce(), "miner": self.getMinerId()})
        return self.chain

    def mineTheNextBlock(self, currentBlock):
        value = currentBlock.getHash() + str(currentBlock.getMinerId())
        nextBlock = block.block(value, 100)
        nextBlock.setMinerId(0)
        text = currentBlock.getHash() + nextBlock.getMinerId() + nextBlock.getNounce()
        hashValue = hashlib.sha256(str.encode(text)).hexdigest()
        nextBlock.setHash(hashValue)
        return nextBlock

    def verifyChain(self, blockchain):
        # Add code here
        return None

def main():
    print("Building a blockchain:\n")
    bc = blockchain("0", 100)
    bc.build(10)

main()