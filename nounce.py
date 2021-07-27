'''
Exercise 2: Nounce
Author: Michelle Xie
'''
import hashlib, string, pickle, os, gzip

class nounce:

    def __init__(self):
        self.alphanumeric = string.ascii_letters + string.digits

    def getNounceValue(self, value, length):
        try:
            nounceLength = length - len(value)
            filename = os.getcwd() + '/' + value + '.txt.gz'
            if os.path.exists(filename):
                print("Looks like you've done some work before. \nLet me reopen it.\n")
                inputFile = open(filename, 'rb')
                decompressData = gzip.decompress(pickle.load(inputFile))
                nList = pickle.loads(decompressData)
                inputFile.close()
                print("Resuming state from {0}".format(filename))
                os.remove(filename)
            else:
                nList = self.buildNounce([], nounceLength)

            while len(nList) > 0:
                n = nList.pop(0)
                if self.tryHash(value, n):
                    return n
                else:
                    nList += self.buildNounce([n], length)
        except KeyboardInterrupt:
            print("Hold on, I'm trying to save your work.")
            numOfFiles = round(len(nList)/1000000)
            lastFile = len(nList) % 1000000
            start = 0
            end = 1000000
            for fileNum in range(numOfFiles):
                compressData = gzip.compress(pickle.dumps(nList[start:end]), compresslevel=1)
                filename = os.getcwd() + '/' + value + '/' + str(fileNum) + '.txt.gz'
                outputFile = open(filename, 'wb')
                pickle.dump(compressData, outputFile)
                outputFile.close()
                start += 1000000
                end += 1000000
            compressData = gzip.compress(pickle.dumps(nList[len(nList)-lastFile:]), compresslevel=1)
            filename = os.getcwd() + '/' + value + '/' + str(numOfFiles+1) + '.txt.gz'
            outputFile = open(filename, 'wb')
            pickle.dump(compressData, outputFile)
            outputFile.close()
            print("State saved to {0}".format(filename))

    def buildNounce(self, nList, length):
        outputList = []

        if len(nList) == 0:
            for character in self.alphanumeric:
                outputList.append(character*length)
            return outputList

        for n in nList:
            characterIndex = 0
            while characterIndex < len(n):
                for alpha in self.alphanumeric:
                    if not (n[characterIndex] == alpha):
                        newNounce = n[0:characterIndex] + alpha + n[characterIndex+1:]
                        if newNounce not in nList:
                            outputList.append(newNounce)
                characterIndex += 1
        return outputList

    def tryHash(self, value, n):
        text = value + n
        hashResult = hashlib.sha256(str.encode(text)).hexdigest()
        if hashResult[0:4] == '0000':
            print("Nounce found: {0}".format(n))
            return True
        print("False: {0}. Search continues.".format(n))
        return False
