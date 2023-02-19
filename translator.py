# Python code to pick a random
# word from a text file
import json

# open the dictionary file
wordFile = open("dictionary.txt", "r")

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

# used to test more translated words
'''
user = input("Enter a phrase: ")

print(englishToMoutain(user))
user = englishToMoutain(user)
print(mountainToEnglish(user))
'''