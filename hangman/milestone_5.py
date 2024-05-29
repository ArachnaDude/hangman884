import json
import random

# from milestone_2 import word_list

class Hangman():
  """
  This class generates the logic for a game of hangman against the computer.

  Attributes:
    word_list (list): the list the game puzzle will be selected from
    word (str): a randomly selected word from the word_list
    word_guessed (list): the current state of the puzzle, initialised as a list of underscores substituting the letters of the puzzle
    num_letters (int): the number of unique letters in the puzzle, case insensitive.
    num_lives (int): the number of lives the player has left, default value = 5
    list_of_guesses (list): the letters the player has already guessed to prevent repeat guesses.
  """
  def __init__(self, word_list, num_lives=5) -> None:
    """
    see help(Hangman) for accurate signature
    """
    self.word_list = word_list
    self.word = random.choice(word_list)
    self.word_guessed = ["_" if char.isalpha() else char for char in self.word["answer"]]
    self.num_letters = len(set(self.word["answer"].lower().replace(" ","")))
    self.num_lives = num_lives
    self.list_of_guesses = []

  def check_guess(self, guess) -> None:
    """
    This function checks the player guess against the puzzle, and responds appropriately

    The function coerces the players guess to lowercase, and searches the answer for that letter, also coerced to lowercase.
    If that letter is present, the function replaces all matched letters in the word_guessed list, in their original cases.

    Args:
      The player's guessed letter
    Returns:
      None 
    """
    guess = guess.lower()
    if guess in self.word["answer"].lower():
      print(f"Good guess! \"{guess}\" is in the word.\n")
      for i in range(len(self.word["answer"])):
        if guess == self.word["answer"][i].lower():
          self.word_guessed[i] = self.word["answer"][i]
      self.num_letters -= 1
    else:
      self.num_lives -= 1
      print(f"Sorry, {guess} is not in the word. \nYou have {self.num_lives} lives left.\n")

  def ask_for_input(self) -> None:
    """
    This function requests and validates user input and - if valid - passes it to the check_guess() function

    Returns:
      None
    """
    while True:
      print(f"Puzzle category: {self.word["prompt"]}")
      print("".join(self.word_guessed))
      guess = input("Guess a letter, and hit enter: \n")
      if len(guess) != 1 or not guess.isalpha():
        print("Invalid letter. Please enter a single alphabetical character.")
        break
      elif guess in self.list_of_guesses:
        print("You already tried that letter\n")
        break
      else:
        self.check_guess(guess)
        self.list_of_guesses.append(guess)
        break
  
def get_puzzle_inputs() -> list:
  """
  This function uses a context manager to open a json list of puzzle prompts and answers for use in the hangman game.

  Returns:
    List: A list of dictionaries, each one containing two keys, 'prompt' and 'answer'. 
  """
  with open("./prompts_and_answers.json", "r") as file:
    word_list = json.load(file)
    return word_list

def play_game(word_list) -> None:
  """
  Plays game of Hangman using the user-provided word list.

  The function instantiates a new game from the Hangman class and starts a game loop.
  The game continues until the player either guesses the puzzle correctly, or runs out of lives.

  Args:
    word_list (list): The user-provided list of words.
  
  Returns:
    None
  """
  num_lives = 7
  game = Hangman(word_list, num_lives)
  while True:
    if game.num_lives == 0:
      print(f"You lost \nThe solution was \"{game.word["answer"]}\"")
      break
    elif game.num_letters > 0:
      game.ask_for_input()
    else:
      print(f"{game.word["answer"]} is correct! \nYou win")
      break
    
if __name__ == "__main__":
  play_game(get_puzzle_inputs())