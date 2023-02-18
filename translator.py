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

wordFile = open("testDict.txt", "r")

wordData = wordFile.read().strip(" ")

words_into_dict = wordData.splitlines()

wordFile.close()

#print(words_into_dict)

# create a list from the .txt file
def listToDict(newList):
    it = iter(newList)
    res_dict = dict(zip(it, it))
    return res_dict

translatedDict = listToDict(words_into_dict)


# get the user input for testing purposes
user = input("Enter a phrase: ")


# change the word with the corresponding word in the dictionary
for words, translated in translatedDict.items():
    user = user.replace(words, translated)

print(user)
