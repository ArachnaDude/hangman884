import random

word_list = ["apple", "banana", "coconut", "dragonfruit", "eggplant"]

word = random.choice(word_list)

print(word)

guess = input("Guess a letter, and hit enter: ")


while True:
  if len(guess) == 1 and guess.isalpha():
    print("Good guess")
    break
  else:
    print("Oops! That is not a valid input")
    guess = input("Guess a letter, and hit enter: ")