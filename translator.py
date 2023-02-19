# Python code to pick a random
# word from a text file
import json


'''
# Open the mountainWords file and putting it into a list
mountainFile = open("MountainWords.txt", "r")

mountainData = mountainFile.read()

mountainData_into_list = mountainData.split("\n")

mountainFile.close()


# Open commonVerbs file and putting it into a list
wordsFile = open("commonWords.txt", "r")

wordsData = wordsFile.read()

wordsData_into_list = wordsData.split("\n")

wordsFile.close()
'''

# opent the dictionary file
wordFile = open("testDict.txt", "r")

wordData = wordFile.read().strip(" ")

words_into_dict = wordData.splitlines()

wordFile.close()

# create a list from the .txt file
def listToDict(newList):
    it = iter(newList)
    res_dict = dict(zip(it, it))
    return res_dict

# dictionary
translatedDict = listToDict(words_into_dict)


# Inverse dictionary
reverseDict = dict(map(reversed, translatedDict.items()))

# translate the english into mountain
def englishToMoutain(user):
    temp = user.split(" ")
    returnUser = []
    for words in temp:
        returnUser.append(translatedDict.get(words,words))

    returnUser = " ".join(returnUser)
    return returnUser

# translate mountain into english
def mountainToEnglish(user):
    temp = user.split(" ")
    returnUser = []
    for words in temp:
        returnUser.append(reverseDict.get(words,words))

    returnUser = " ".join(returnUser)
    return returnUser

