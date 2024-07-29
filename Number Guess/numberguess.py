import random
import math

lower = int(input("Enter lower number : "))
higher = int(input("Enter higher number : "))

random_number = random.randint(lower,higher)
print("Here it is : ",random_number)
count = 0

while True:
    now = int(input("What is your guess ? Ans: "))
    if(now==random_number):
        print("Congratulations.You guessed it within ",count," times.")
        break
    else:
        count+=1
        if now<random_number:
            print("Your enter too less.")
        elif now>random_number:
            print("You enter too high.")


