import random

lives_allowed = 11
lives = 0
letters = [""]
wordlist = [
"lion", "umbrella", "window", "computer", "glass", "juice", "chair", "desktop",
 "laptop", "dog", "cat", "lemon", "cabel", "mirror", "hat"
           ]
blanks = [""]



print ("Welcome to hangman")

word = random.choice(wordlist)

lengte = len(word)


for i in range(lengte):
    blanks.append("_")

print (''.join(map(str, blanks)))
