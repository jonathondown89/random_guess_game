import random
 #intro to statement
print(f"It's time to play a guessing game, where you will have 3 attempts to guess"
      f"a random Integer between 1 and 10.")

#setting answer as random int 
answer = random.randint(1, 10)

#loop to evaluate guess
for attempt in range(3):
    print("Please type your guess: ")
    guess = int(input())
    if guess == answer:
        print("You got it! well done the Integer was", answer, ".")
        break
    if guess > answer:
        print("The guess was too high!")
    elif guess < answer:
        print("The guess was too low!")
else:
    print("Sorry you are not a winner, as you did not guess that the Integer was",
          answer, "after the three attempts")
