# Python code to pick a random
# word from a text file
import random
  
# Open the mountainWords file and putting it into a list
mountainFile = open("MountainWords.txt", "r")

mountainData = mountainFile.read()

mountainData_into_list = mountainData.split("\n")

mountainFile.close()


# Open commonVerbs file and putting it into a list
verbsFile = open("commonVerbs.txt", "r")

verbsData = verbsFile.read()

verbsData_into_list = verbsData.split("\n")

verbsFile.close()


user = input("Enter a phrase: ").lower().split(" ")
index = 0;

for index, words in enumerate(user):
    if words in verbsData_into_list:
        print("found")
        newWord = random.choice(mountainData_into_list)
        print(newWord)
        user[index] = newWord
        print("changing ",words, "into ", newWord)

print(user)

