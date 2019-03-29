import random

lives_allowed = 11
lives = 0
letters = ["a"]
wordlist = [
"lion", "umbrella", "window", "computer", "glass", "juice", "chair", "desktop",
 "laptop", "dog", "cat", "lemon", "cabel", "mirror", "hat"
           ]
blanks = [""]
nieuw = False


print ("Welcome to hangman")

word = random.choice(wordlist)

lengte = len(word)

for i in range(lengte):
    blanks.append("_")
    
print (' '.join(map(str, blanks)))




while lives_allowed > lives:
    guess = input("Choose a letter: ")
    if len(guess) > 1:
        print ("please enter 1 letter")
    if guess.isalpha() == False:
        print ("please only use letters")
    if guess.lower() in letters :
        print("you've already guessed that letter")
    elif guess.lower != letters :
        print (letters)
        letters.append(guess)
     


        
    
    
    

    
