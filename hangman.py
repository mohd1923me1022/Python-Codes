import random

words = ["independently", "banana", "weather", "country", "amazingly"]
letters = [] #to store sliced letters or random word
copy = [] #contains all the right guessed words
check =[] #to store entered words

def duplicate(enter): #to check dublicate entries
    if enter in check:
        print("You entered the same letter")
        return False
    else:
        check.append(enter) #storing unique entries in check[]
        return True

print('''****Welcome to hangman game****\n 
Instructions: 
A random word has been chosen, you need to enter one letter at a time to guess the word. 
If you guess the word correctly, it will fill empty spaces\n''')

word = random.choice(words)

for alpha in word:
    letters.append(alpha) #splitting words into letters
    copy.append("_") #initializing copy with _

guess=5
while guess>0:
    print(f"{guess} guesses left.")
    enter = input("Guess a letter.\n").lower().strip()
    if duplicate(enter): #block only runs if true
        for i in range(len(word)):
            if enter == letters[i]:#checking if user entered word if present in the word
                copy[i] = enter #filling correct letter in every position 
             
        if enter in letters: #telling user that the letter is present in the word
            print(f"Yes '{enter}' is present in the word in following position(s)\n{copy}")
        else:
            print("Try something else.")
            guess-=1 #decrimemt guess for every wrong guess
               
        if copy==letters: #checking if user guessed the entire word
            print(f"You guessed the word correctly! Thanks for playing....")
            break
               
if copy !=letters: #checking if user didnt guess the entire word
    print(f"Better luck next time....The word was '{word}'.")