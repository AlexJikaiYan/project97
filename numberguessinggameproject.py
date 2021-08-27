chances = 0
while chances < 5:
    if not chances < 5: 
        print("the number is 9")
numberguess=int(input("enter a number from 1-10:")) 
if (numberguess>9) :
    print("Your guess was too high: Guess a number below",(numberguess))
    numberguess=(input("enter a lower number:"))
    chances=chances+1
elif(numberguess<9) :
    print("Your guess was too low: Guess a number below",(numberguess))
    numberguess=(input("enter a higher number:"))
    chances=chances+1
else:
            print("You guessed the right number")
          break
 
