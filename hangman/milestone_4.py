import random

from milestone_2 import word_list

class Hangman():
  def __init__(self, word_list, num_lives=5) -> None:
    self.word_list = word_list
    self.word = random.choice(word_list)
    self.word_guessed = ["_" for letter in self.word]
    self.num_letters = len(set(self.word))
    self.num_lives = num_lives
    self.list_of_guesses = []

  def check_guess(self, guess):
    guess = guess.lower()
    if guess in self.word:
      print(f"Good guess! \"{guess}\" is in the word.")
      self.word_guessed = [guess if self.word[i] == guess else self.word_guessed[i] for i in range(len(self.word))]
      self.num_letters -= 1
      print(self.word_guessed)

  def ask_for_input(self):
    while True:
      guess = input("Guess a letter, and hit enter: \n")
      if len(guess) != 1 or not guess.isalpha():
        print("Invalid letter. Please enter a single alphabetical character.")
      elif guess in self.list_of_guesses:
        print("You already tried that letter")
      else:
        self.check_guess(guess)
        self.list_of_guesses.append(guess)
  

h = Hangman(word_list)
h.ask_for_input()
