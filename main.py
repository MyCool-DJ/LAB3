#guessing game
from random import randint #using a from [command] a built in random function (in Python 3.8) import [command] randint a built in method  to get a rand[om]int[ger] 

print ("In this program you will enter a number between 1 - 100."
       "\nAfter the computer will try to guess your number!") #This print statement displays text in the console to provide the user information regarding what the program does.

number = 0 # a golbal variable with the vaule 0 assigned before the code block which win then store a local variable

while number < 1 or number >100: # a while loop for the condition of the [random] integer being less than one or greater than 100
    number = int(input("\n\nEnter a number for the computer to guess: ")) # the local variable stores the integer asked for the user to input
    if number > 100: # this if statement checks that the number is greater than 100, users can try and break the program or not read the instructions
        print ("Number must be lower than or equal to 100!")
    if number < 1: #this if statement checks if the number [entered] is less than 1 if it is it prints the statement
        print ("Number must be greater than or equal to 1!")

guess = randint(1, 100) #this 

print ("The computer takes a guess...", guess)

while guess != number:
    if guess > number:
        guess -= 1
        guess = randint(1, guess)
    else:
        guess += 1
        guess = randint(guess, 100)
    print ("The computer takes a guess...", guess)

print ("The computer guessed", guess, "and it was correct!")