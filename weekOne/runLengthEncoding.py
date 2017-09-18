from collections import OrderedDict
# import pdb
def RLE (fileName):
    readFile = open(fileName, "r")
    text = readFile.read().strip()
    readFile.close()

    print "Print out input string: ", text
    # fileDict = OrderedDict()
    encoded = []
    previous = ''
    counter = 0
    print "length", len(text)

    for i, letter in enumerate(text):
        print i
        print letter

        if previous != letter:
            if not previous:
                previous = letter
                counter = counter+1
            else:
                pair = (previous, counter)
                encoded.append(pair)
                previous = letter
                counter = 1
        else:
            previous = letter
            counter = counter+1

        if i == len(text)-1:
            pair = (previous, counter)
            encoded.append(pair)

    print encoded
    return encoded

RLE ("sample.txt")

def decoder(encodedStr):
    decoded = ''
    for letter, count in encodedStr:
        print letter
        print count
        i = 0
        while i < count:
            i += 1
            decoded += letter
    print decoded
    return decoded

decoder(RLE ("sample.txt"))
