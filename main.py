import os
import random
import logging
from hangman_words import word_list
from hangman_art import logo, stages

logging.basicConfig(level = logging.INFO)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
logging.info(f'chosen_word = {chosen_word}.')

end_of_game = False
lives = 6
guesses = []
display = []
for _ in range(word_length):
    display += "_"

print(logo)

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    # os.system('clear')

    if guess in guesses:
        print(f"'You already guessed '{guess}'")
        continue
    else:
        guesses.append(guess)

    for position in range(word_length):
        letter = chosen_word[position]
        logging.debug(
            f"position = {position}, letter = {letter}, guess = {guess}")
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"'{guess}' is not in the word, you lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose. The word was '{chosen_word}'")
    else:
        print(f"Well done '{guess}' is in the word.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
