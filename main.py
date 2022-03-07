import random
import Hangman_art
import hangman_words
#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)


end_of_game = False
lives = 6



#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(Hangman_art.logo)
#Testing code

print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
letters_that_used = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess not in letters_that_used:
        letters_that_used.append(guess)
    else:
        print(f"You had entered {guess} before. Please enter a different number")
        continue
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"{guess} is not in chosen word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("YOU LOSE")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("YOU WIN")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(Hangman_art.stages[lives])