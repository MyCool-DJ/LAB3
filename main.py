#guessing game
print("The Guessing Game")
print("=="*20)
from random import randint #using a from [command] a built in random function (in Python 3.8) import [command] randint a built in method  to get a rand[om]int[ger] 

print ("In this program you will enter a number between 1 - 100."
				"\nAfterwards the computer will try to guess your number!") #This print statement displays text in the console to provide the user information regarding what the program does.

number = 0 # a golbal variable with the vaule 0 assigned before the code block which win then store a local variable

while number < 1 or number >100: # a while loop for the condition of the [random] integer being less than one or greater than 100
			number = int(input("\n\nEnter a number for the computer to guess: ")) # the local variable stores the integer asked for the user to input
if number > 100: # this if statement checks that the number is greater than 100, users can try and break the program or not read the instructions
						print ("Number must be lower than or equal to 100!")
if number < 1: #this if statement checks if the number [entered] is less than 1 if it is it prints the statement
						print ("Number must be greater than or equal to 1!")

guess = randint(1, 100) #this golbal variable stores a rand[om]int[ger] number between 1 and 100 because the start stop values are entered inside the parentheses as our parameters. This the computer [program] guessing a number

print ("The computer takes a guess...", guess) # this tells the user what the program is doing

while guess != number: # a while loop, with a condition that checks if the [random] guess gobal variable is not equal to the number entered by our user.
		if guess > number: #if statement with guess greater than the number the program excutes this indented code block within the while loop
					guess -= 1 # the program now knows that the number is at least one whole number that its guess
					guess = randint(1, guess) #so now it updates the local variable with the pervious guess minus one to now store the randint with the parameters (1 as a min and the updaetd guess var as the new max to generate a random num)
					print ("The computer takes a guess...", guess)
		else:
					guess += 1 #if the first condition is not met we move to this part of the code block meaning the guess (random number import) was less than the users input number. This will add one to the guess var and then store the guess local var with the updated value
					guess = randint(guess, 100) #now with the updated var the guess var is updated with another rad[om]int[ger] with the parameters within the parentheses being the min and 100 being the max
					print ("The computer takes a guess...", guess)


print ("The computer guessed", guess, "and it was correct!")
		#once the condition is met a boolen vaule of False is expressed meaning the while loop code block is skipped printing this statement with the guess value displayed.

