'''
Exercise 2: Nounce
Author: Michelle Xie
'''
import hashlib, string, pickle, os, gzip

def saveFile(nList, value, increment):
    print("Hold on, I'm trying to save your work.")
    numOfFiles = round(len(nList)/increment) 
    if numOfFiles > 0:
        start = 0
        end = increment
        os.chdir(os.getcwd())
        os.mkdir(value)
        os.chdir(os.getcwd() + '/' + value)
        for fileNum in range(numOfFiles):
            compressData = gzip.compress(pickle.dumps(nList[start:end]), compresslevel=1)
            filename = str(fileNum) + '.txt.gz'
            outputFile = open(filename, 'wb')
            pickle.dump(compressData, outputFile)
            outputFile.close()
            print("Progress: {0}%.".format(fileNum/numOfFiles * 100))
            start += increment
            end += increment

        lastFile = len(nList) % increment
        compressData = gzip.compress(pickle.dumps(nList[len(nList)-lastFile:]), compresslevel=1)
        filename = str(lastFile) + '.txt.gz'
        outputFile = open(filename, 'wb')
        pickle.dump(compressData, outputFile)
        outputFile.close()
        print("States saved to {0}".format(filename))
    else:
        compressData = gzip.compress(pickle.dumps(nList), compresslevel=1)
        filename = value + '.txt.gz'
        outputFile = open(filename, 'wb')
        pickle.dump(compressData, outputFile)
        outputFile.close()
        print("States saved to {0}".format(filename))


def loadFile(value, filename):
    print("Looks like you've done some work before. \nLet me reopen it.\n")
    nList = []
    os.chdir(filename)
    count = 1
    length = len(os.listdir(filename))
    for f in os.listdir(filename):
        inputFile = open(f, 'rb')
        decompressData = gzip.decompress(pickle.load(inputFile))
        nList += pickle.loads(decompressData)
        inputFile.close()
        os.remove(f)
        print("Progress: {0}%.".format(count/length * 100))
        count += 1
    print("Resuming state from {0}".format(filename))
    return nList


def sha256hash(value, n):
    text = value + n
    hashResult = hashlib.sha256(str.encode(text)).hexdigest()
    if hashResult[0:4] == '0000':
        print("Nounce found: {0}".format(n))
        return True
    print("False: {0}. Search continues.".format(n))
    return False

class nounce:

    def __init__(self):
        self.alphanumeric = string.ascii_letters + string.digits

    def getNounceValue(self, value, length):
        try:
            nounceLength = length - len(value)
            filename = os.path.join(os.getcwd(), value)
            if os.path.exists(filename):
                nList = loadFile(value, filename)
                os.chdir('..')
                os.rmdir(filename)
            else:
                nList = self.buildNounce([], nounceLength)

            while len(nList) > 0:
                n = nList.pop(0)
                if sha256hash(value, n):
                    return n
                else:
                    nList += self.buildNounce([n], length)
        except KeyboardInterrupt:
            return saveFile(nList, value, 100000)

    def buildNounce(self, nList, length):
        outputList = []

        if len(nList) == 0:
            for character in self.alphanumeric:
                outputList.append(character*length)
            return outputList

        n = nList[0]
        characterIndex = 0
        while characterIndex < len(n):
            for alpha in self.alphanumeric:
                if not (n[characterIndex] == alpha):
                    newNounce = n[0:characterIndex] + alpha + n[characterIndex+1:]
                    outputList.append(newNounce)
            characterIndex += 1
        nList.pop(0)
        return outputList

