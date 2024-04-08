import csv
import random

print("Welcome to Wordle!"
      "Here you can play a game of Wordle \n"
      ""
      "Instructions:\n"
      "You start by guessing a 5 letter word that will reveal whether a character has been guessed correctly\n"
      "as well as showing if the character is in the word\n"
      ""
      "For a character that has been guessed correctly it will display as green\n"
      "otherwise it will display as the colour orange\n"
      ""
      "Unforunately you can guess some letters wrong therefore if the colour of the square does not change\n"
      "it will display as gray.\n "
      ""
      "Good Luck!\n")

all_words = []
with open("5_letter_words.csv") as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
            all_words.append(row)
      print(all_words)

total_words = len(all_words)

random_word_idx = random.randint(0, total_words-1)
wordle_word = all_words[random_word_idx]
print(wordle_word)
storage = []
for word in wordle_word:
      for char in word:
            storage.append(char)

user_input = list(input("Please guess a five letter word"))

print(user_input)

i = 0
for i in range(0,5):
      if user_input[i] == storage[i]:
            print("Correct!")
      else:
            print("Incorrect!")
