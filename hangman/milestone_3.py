from milestone_2 import word

print(word)

while True:
  guess = input("Guess a letter, and hit enter: ")

  if len(guess) == 1 and guess.isalpha():
    if guess in word:
      print(f"Good guess! {guess} is in the word")
    else:
      print(f"Sorry, {guess} is not in the word. Try again")
    break
  else:
    print("Invalid letter. Please enter a single, alphabetical character")