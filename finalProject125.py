# Import Dependencies
import hashlib
import time


#recursiveSolve is the function to recursively solve algorithms
#charList contains the character universe from which enumerations and hashes are computed
#tempTry has the string constructed so far
#hashedString is the hash we are trying to match
#fuse is the length of password we are looking to match. We must use a fuse because
#otherwise the recursive tree will call indefinitely and there would be no base case
def recursiveSolve(charList, tempTry, hashedString, fuse):
    #we must remove the endline and spaces in order to get a matched hash
    hashedString = hashedString.rstrip()
    #if we aren't to the correct length, call all possible next character strings
    #from our base tempTry
    if len(tempTry) < fuse:
        tempResult = ""
        for x in charList:
            tempResult = recursiveSolve(charList, (tempTry + x), hashedString, fuse)
            #if we get a match, return the match immediately
            if tempResult != None:
                return tempResult
        return None
    #if the fuse is the right length, we have to compute the hash and see if we have a match
    elif fuse == len(tempTry):
        #check if the hashes match, if so return the password
        if hashlib.md5((tempTry).encode('utf-8')).hexdigest() == hashedString :
            return tempTry
        #if not, don't return anything
        return None

def main():
    try:
        hashFile = open("hashes.txt","r")
        hashList = hashFile.readlines()
        #complete list of possible characters
        #alphanumericList = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
        #only the special characters used in the test password
        alphanumericList = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '@']
        #only lowercase characters
        #alphanumericList = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
        solved = False;

        #this iterates through all hashes in the input list
        for hashedLine in hashList:
            startTime = time.time()
            solved = False;

            #I make the algorithm stop trying after 10 characters because anything
            #longer would never finish. This is pretty arbitrary though and it just
            #needs to be long enough
            for i in range(1, 10):
                if not solved:
                    tempcompare = ""
                    result = recursiveSolve(alphanumericList, tempcompare, hashedLine, i)
                    if result != "NULL" and result != None:
                        solved = True;

                        print "For the hashed password " + hashedLine.rstrip()
                        print "The cracked password is " + result
                        print "And the time to solve it was (in seconds)"
                        print time.time()-startTime
                        print "\n"
    except ValueError:
        print "Done!"

if __name__ == "__main__":
    main()
