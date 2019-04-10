# Import Dependencies
import hashlib
from multiprocessing import Process
import time


def recursiveSolve(charList, tempTry, hashedString, fuse):
    #print tempTry
    #print fuse
    #print "\n"
    hashedString = hashedString.rstrip()

    if len(tempTry) < fuse:
        tempResult = ""
        for x in charList:
            #print x
            tempResult = recursiveSolve(charList, (tempTry + x), hashedString, fuse)
            #print tempResult
            if tempResult != None:
                return tempResult
        #print "NONE"
        return None

    elif fuse == len(tempTry):
        for x in charList:
            #print "correct length match"
            #print hashlib.md5((tempTry + x).encode('utf-8')).hexdigest() + " vs " + hashedString

            if hashlib.md5((tempTry + x).encode('utf-8')).hexdigest() == hashedString :
                print tempTry + x + " answer"
                return (tempTry+x)


        #print "no answer"
        return None

def main():

    hashFile = open("hashes.txt","r")
    hashList = hashFile.readlines()
    #complete list of possible characters
    #alphanumericList = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
    #only the special characters used in the test password
    alphanumericList = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '@']
    #only lowercase characters
    #alphanumericList = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
    solved = False;
    for hashedLine in hashList:
        startTime = time.time()

        solved = False;
        for i in range(0, 6):
            if not solved:
                tempcompare = ""
                result = recursiveSolve(alphanumericList, tempcompare, hashedLine, i)
                if result != "NULL" and result != None:
                    solved = True;
                    print hashedLine
                    print result
                    print "time to solve was "
                    print time.time()-startTime

    #print(recursiveSolve(alphanumericList, "", hashedLine, 10))

if __name__ == "__main__":
    main()
