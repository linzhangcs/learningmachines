from sys import argv
from collections import OrderedDict

# he dict() constructor builds dictionaries directly from sequences of key-value pairs:
#
# >>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
# {'sape': 4139, 'jack': 4098, 'guido': 4127}

# stuff = dict([{'w': 2, 'o': 3 }])
# stuff2 = {'w': 2, 'o': 3 }
# stuff3 = OrderedDict()
# stuff3['w'] = 3
# stuff3['o'] = 9
#
# print "values: ", stuff.items()
# print stuff3
# print stuff3.keys()
# print stuff3.values()
#
# for key in stuff:
#     print key
#     print stuff[key]

def printOut(fileName):
    readFile = open(fileName, "r")
    text = readFile.read()
    readFile.close()

    print "Print out input string again: ", text

    fileDict = OrderedDict()
    current = ''
    counter = 0
    i = 0

    for letter in text:

        if i == 0:
            current = letter
            counter = counter + 1
        elif current == letter:
            current = letter
            counter = counter + 1
        else:
            print i
            print letter
            fileDict[current] = counter
            current = letter
            counter = 1
        i = i+1

    print fileDict
    return fileDict

printOut("sample.txt")



# inputNumber = argv
#
# print "the number is: ", inputNumber
# # This is a comment
# print "This is the beginning of the file"
#
# cars = 100
# space_in_a_car = 4.0
# drivers = 30
# passengers = 90
# topic = "This is okay"
#
# average_passengers_per_car = passengers / drivers
#
# print "There are", cars, "cares available."
# print "Let's talk about %s." % topic
# print "We need to put about", average_passengers_per_car, "in each car."
# print "Why am I doing this? %d, %d, and, %s"%(cars, passengers, topic)
#
# x = "There are %d types of people." % 10
# binary = "binary"
# doNot = "dont"
# y = "There who know %s and those %s." %(binary, doNot)
#
# print x
# print y
#
# print "I said: %r" % x
#
# input = raw_input("Name? ")
# print "Your name is %s "%input


        # if i == 0:
        #     current = letter
        #     counter = counter + 1
        # elif current == letter:
        #     current = letter
        #     counter = counter + 1
        # elif current != letter:
        #     fileDict[current] = counter
        #     current = letter
        #     counter = 1
        #
        #     i == len(text) - 1
        #     pdb.set_trace()
        #     print "last", len(text) -1
        #     print "letter", letter
        #     print current
        #     fileDict[current] = counter

        # if i == 0:
        #     current = letter
        #     counter = counter + 1
        # elif i < len(text)-2:
        #     if current == letter:
        #         current = letter
        #         counter = counter + 1
        #     else:
        #         # fileDict[current] = counter
        #         pair = (letter, counter)
        #         encoded.append(pair)
        #         current = letter
        #         counter = 1
        # else:
        #     if current == letter:
        #         current = letter
        #         counter = counter + 1
        #     else:
        #         # fileDict[current] = counter
        #         pair = (letter, counter)
        #         encoded.append(pair)
        #         current = letter
        #         counter = 1
