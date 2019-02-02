from difflib import SequenceMatcher
import json

#we need to parse the jason string, so we can be able to use its content as a python dico
def get_json():
    with open("./data.json","r") as data_file:
        return json.loads(data_file.read())


def getInput():
    print("\n____Dictionary____\n")
    return input('Enter word: ')

def find_word(word, data):
    if word in data.keys():
        return True
    return False


def findSimilarWord(word, data):
    lst = []
    for w in data.keys():
        if SequenceMatcher(None, w, word).ratio()  > 0.7:
            lst.append(w)
    return lst


def getMaxSimilarityRation(word,lst):
    max = 0
    for w in lst:
        if SequenceMatcher(None, w, word).ratio() > max:
            max = SequenceMatcher(None, w, word).ratio()
            suggestedWord = w
    return suggestedWord


def isTheOne(userInput):
    userInput = userInput.lower()
    if userInput == "yes" or userInput == "y":
        return True
    return False


def printDefinition(arr):
    for i in range(len(arr)):
        print("%d. %s\n"%(i+1, arr[i]))

#case : if the user enters Pariis
def get_definition(word, data):
    x = find_word(word, data)
    if x == True:
        printDefinition(data[word])
    else:
        word = word.lower()
        x = find_word(word, data)
        if x == True:
            printDefinition(data[word])
        else:
            lst = findSimilarWord(word, data)
            if(lst):
                y = getMaxSimilarityRation(word,lst)
                print("this word does not exist\nDo you mean: %s ?"%y)
                if isTheOne(input("[Yes / No]\n")):
                    printDefinition(data[y])
                else:
                    print("there is no such a word, please double check it ;)")
            else:
                print("there is no such a word, please double check it ;)")


data = get_json()
word = getInput()
get_definition(word, data)
