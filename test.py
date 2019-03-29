import random

lives = 11
letters = []
wordlist = [
"lion", "umbrella", "window", "computer", "glass", "juice", "chair", "desktop",
 "laptop", "dog", "cat", "lemon", "cabel", "mirror", "hat"
           ]
blanks = []
nieuw = False
woord = []


print ("Welcome to hangman\nThe goal of the game is to guess the word, you have %s lives \nUse the following commands to play the game:\nTo see the letters you've already used: letters\nTo see your lives left: lives" % str(lives))
print ("")
print("")
"""word = random.choice(wordlist)"""
word = "apple"
game = True

lengte = len(word)

for i in word:
    woord.append(i)
     
for i in range(lengte):
    blanks.append("_")
    

print ("The length",' '.join(map(str, blanks)))
print ("")



while game == True:
    fout = False
    guess = input("Choose a letter: ")
    if len(guess) > 1 and guess != lives and guess != letters:
        print ("please enter 1 letter")
    if guess.isalpha() == False:
        print ("please only use letters")
    if guess.lower() in letters :
        print("you've already guessed that letter")
    elif guess.lower != letters :
        letters.append(guess)
    
        for position, item in enumerate(woord):
            if item == guess.lower():
                del blanks [position]
                blanks.insert(position, guess)
            elif item != guess.lower():
                fout = True  
                
        if fout ==  True:
            lives -= 1
            print ("helaas, dat is niet goed")
    print (' '.join(map(str, blanks)))
    print ("")



    
    if lives == 0:
        print ("game over")
        game = False
    
        
                
        
                
                
                
                