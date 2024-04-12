import csv
import random
from rich.console import Console
from rich.prompt import Prompt

SQUARES = {
    'correct_place': '🟩',
    'correct_letter': '🟨',
    'incorrect_letter': '⬛'
}

ALLOWED_GUESSES = 6


def correct_place(letter):
    return f'[black on green]{letter}[/]'


def correct_letter(letter):
    return f'[black on yellow]{letter}[/]'


def incorrect_letter(letter):
    return f'[black on white]{letter}[/]'


def chosen_word():
    all_words = []
    with open("5_letter_words.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            all_words.append(row[0])  # Extracting the word from the row
    total_words = len(all_words)

    random_word_idx = random.randint(0, total_words - 1)
    wordle_word = all_words[random_word_idx].upper()
    return wordle_word


def check_guess(user_input, storage):
    guessed = []
    wordle_pattern = []
    for i, char in enumerate(user_input):
        if user_input[i] == storage[i]:
            guessed.append(f'[black on green]{SQUARES["correct_place"]}[/]')
            wordle_pattern.append(SQUARES['correct_place'])
        elif char in storage:
            guessed.append(f'[black on yellow]{SQUARES["correct_letter"]}[/]')
            wordle_pattern.append(SQUARES['correct_letter'])
        else:
            guessed.append(f'[black on white]{SQUARES["incorrect_letter"]}[/]')
            wordle_pattern.append(SQUARES['incorrect_letter'])
    return "".join(guessed), "".join(wordle_pattern)


def game(console, chosen_word):
    end_of_game = False
    already_guessed = []
    full_wordle_pattern = []
    all_words_guessed = []

    while not end_of_game:
        user_guess = Prompt.ask("Please guess a five letter word").upper()
        while len(user_guess) != 5 or user_guess in already_guessed:
            if user_guess in all_words_guessed:
                console.print("[red]You've already guessed this word!!\n[/]")
            else:
                console.print('[red]Please enter a 5-letter word\n[/]')
            user_guess = input("Please enter a 5-letter word: ").upper()
        already_guessed.append(user_guess)
        guessed, pattern = check_guess(user_guess, chosen_word)
        all_words_guessed.append(guessed)
        full_wordle_pattern.append(pattern)

        console.print(*all_words_guessed, sep="\n")

        if user_guess == chosen_word or len(already_guessed) == ALLOWED_GUESSES:
            end_of_game = True
    if len(already_guessed) == ALLOWED_GUESSES and user_guess != chosen_word:
        console.print(f'\n[red]WORDLE X/{ALLOWED_GUESSES}[/]')
        console.print(f'\n[green]Correct Word: {chosen_word}[/]')
    else:
        console.print(f'\n[green]WORDLE {len(already_guessed)}\{ALLOWED_GUESSES}[/]\n')
    console.print(*full_wordle_pattern, sep="\n")


if __name__ == "__main__":
    console = Console()
    chosen_word = chosen_word()
    console.print("Welcome to Wordle!"
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
    game(console, chosen_word)
