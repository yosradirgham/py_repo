from difflib import SequenceMatcher
import json

#we need to parse the jason string, so we can be able to use its content as a python dico
def get_json():
    with open("./data.json","r") as data_file:
        return json.loads(data_file.read())


def find_word(word, data):
    if word in data:
        return True
    return False


def similarity(str1, str2):
    return SequenceMatcher(None, str1, str2).ratio()


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
    if userInput == "yes":
        return True
    return False


def get_definition():
    data = get_json()

    print("\n____Dictionary____\n")
    word = input('Enter word: ')
    word = word.lower()

    x = find_word(word, data)

    if x == True:
        print(data[word])
    else:
        lst = findSimilarWord(word, data)
        if(lst):
            y = getMaxSimilarityRation(word,lst)

            print("this word does not exist\n")
            print("Do you mean: "+ y +" ?")
            if isTheOne(input("[Yes / No]\n")):
                print(data[y])
        else:
            print("there is no such a word, please double check it ;)")


get_definition()
