import random
num=random.randint(1,100)
print('''****Welcome to number guessing game. You have to guess the number by following instructions given in each step****\n''')

guess=int(input("Enter a number between 1 to 100 to guess\n"))

for i in range(1,8):
    if (guess==num):
        print(f"Congratulations! You guessed it in {i} guesses")
        break    
    elif(guess>num):
        guess=int(input(f"Try a SMALLER number\n"))
    elif(guess<num):
        guess=int(input("Try a BIGGER number\n"))
  
if(i==7 and guess!=num):                      print("You Lost! Number was",num)

with open("highscore.txt","r") as f:
    highscore=f.read()
    if(str(i)<highscore):
        with open("highscore.txt","w") as f:
            f.write(str(i))