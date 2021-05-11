# List of valid words for the game
schengen_countries = ["Austria", "Belgium", "Czechia", "Denmark", "Estonia", "Finland",
                      "France", "Germany", "Greece", "Hungary", "Iceland", "Italy", "Latvia",
                      "Liechtenstein", "Lithuania", "Luxembourg", "Malta", "Netherlands",
                      "Norway", "Poland", "Portugal", "Slovakia", "Slovenia", "Spain",
                      "Sweden", "Switzerland"]

# Define different hangman stages as unsuccessful guesses
hangman_phases = ["""
    _______
    |     |
    |     
    |    
    |        """ , """
    _______
    |     |
    |     O
    |    
    |        """ , """
    _______
    |     |
    |     O
    |     |
    |        """ , """
    _______
    |     |
    |     O
    |    -|
    |        """ , """
    _______
    |     |
    |     O
    |    -|-
    |        """ , """
    _______
    |     |
    |     O
    |    -|-
    |    /   """ , """
    _______
    |     |
    |     O
    |    -|-
    |    / \\"""]

# Random selection from schengen_countries
import random
secret_word = random.choice(schengen_countries).upper()

# Welcoming message and initial hangman print + spaces to be guessed
print("Hey! Let's play Hangman. \n"
      "I will pick one of the Shengen countries and \n"
      "you will need to guess which one is it. \n"
      "You can only guess 1 letter at a time or the whole word! \n"
      "Good luck! \n"
      + hangman_phases[0] + "\n"
        "      " + "_" * len(secret_word) + "\n")

def play(secret_word):
    tries = 0
    # tries can go from 0 to 6 (stages of the hangman)
    guessed_letters = []
    secret_word_guesses = "_"*len(secret_word)
    guessed_words = []

    # Function for the hangman print + secret_word_guesses to print out after every guess
    def hangman_status():
        print(hangman_phases[tries])
        print("      " + secret_word_guesses)

    # Function for the game over print out when tries = 6
    def game_over():
        print(hangman_phases[6])
        print("      " + secret_word_guesses)
        print("""
        ************************* \n
        *** G A M E   O V E R *** \n
        ************************* \n
        The secret word was → """ + secret_word)

    while "_" in secret_word_guesses and tries < 6:
        # ask for the user input
        guess = input("Your guess -> ").upper()
        #Input is 1 letter which is part of the secret word
        if len(guess) == 1 and guess.isalpha() == True and guess in secret_word:
            #The letter has already been inputed bu the user
            if guess in guessed_letters:
                print("You already guessed this letter")
            #It's a new letter
            else:
                guessed_letters.append(guess)
                #check each letter of the word to be guessed if in guessed_letters
                #Create a new variable to use it as temporary for all letter guessed substitutions
                secret_word_replacement = ''
                for i in range(len(secret_word)):
                    if secret_word[i] in guessed_letters:
                        secret_word_replacement += secret_word[i]
                    else:
                        secret_word_replacement  += "_"

                secret_word_guesses = secret_word_replacement
                hangman_status()

        #Input is a letter which is not in our secret word
        elif len(guess) == 1 and guess.isalpha() == True and guess not in secret_word:
            if guess in guessed_letters:
                print("You already guessed this letter")
            else:
                if tries < 5:
                    tries += 1
                    guessed_letters.append(guess)
                    hangman_status()
                else:
                    game_over()
                    break

        #Input is a word
        elif len(guess) > 1 and guess.isalpha()==True:
            #The word has already been inputted
            if guess in guessed_words:
                print("You already guessed this word!")
            #New word inputted
            else:
                guessed_words.append(guess)
                #The word is not our secret word
                if guess != secret_word:
                    if tries <5:
                        tries += 1
                        guessed_letters.append(guess)
                        hangman_status()
                    else:
                        game_over()
                        break
                #Bingo! The word has been guessed!
                else:
                    secret_word_guesses = secret_word
                    hangman_status()

        # The input is not a letter or a word:
        elif guess.isalpha() == False:
            print("Your input is not valid")

    #message to be printed if the word has been guessed
    if secret_word == secret_word_guesses:
        print("Excelent! You guessed the secret country :)")

play(secret_word)