while True:
  guess = input("Guess a letter, and hit enter: ")

  if len(guess) == 1 and guess.isalpha():
    print("Good guess")
    break
  else:
    print("Invalid letter. Please enter a single, alphabetical character")