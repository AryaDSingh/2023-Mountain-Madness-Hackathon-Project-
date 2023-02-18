# Python code to pick a random
# word from a text file
import random
  
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


user = input("Enter a phrase: ").lower().split(" ")

for index, words in enumerate(user):
    if words in wordsData_into_list:
        newWord = random.choice(mountainData_into_list)
        user[index] = newWord


returnString = " ".join(user)

user = returnString

print(user)

