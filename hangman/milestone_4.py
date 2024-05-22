import random

class Hangman():
  def __init__(self, word_list, num_lives=5) -> None:
    self.word_list = word_list
    self.word = random.choice(word_list)
    self.word_guessed = [] #Todo - list of the letters in the word with _ for each letter not guessed
    self.num_letters = None #Todo - number of unique letters in the word that have not been guessed yet 
    self.num_lives = num_lives
    self.list_of_guesses = []