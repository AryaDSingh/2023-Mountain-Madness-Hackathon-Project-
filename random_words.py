# Python code to pick a random
# word from a text file
import random
  
# Open the file in read mode
with open("MountainWords.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))
  
    # print random string
   # print(random.choice(words))

print(I love )