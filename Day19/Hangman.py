import random
from json import load

def get_word():
    with open('C:\\Users\\rushi\\Documents\\pythonprojects\\Hangman\\words.json') as json_file:
        data = load(json_file)
        #print(data)
    wordArray = data["word_list"]
    word = random.choice(wordArray)
    word = word.upper()
    return word

def play(word):
    print("Welcome ! To the Hangman Game .\n")
    print("Computer will choose random word from a list .\n")
    print("You have to type a letter (one at a time)")
    print("Which you think may be present i the word .")
    input("Press Enter to play :")

    tries = 6
    word_to_guess = get_word()
    guessed_word = "_"*len(word_to_guess)
    used_letter = set()

    print(f"{guessed_word}\n")
    print(f"Life : {tries}")
    print(display_hangman(tries-1))
    print()
    print("Used letters    :", *used_letter)
    while tries:
        guessed_letter = input("> ").strip()
        used_letter.add(guessed_letter)

        if guessed_letter in word_to_guess:
            temp = ""
            for i in range(len(word_to_guess)):
                if (word_to_guess[i] == guessed_word[i]):
                    temp += word_to_guess[i]
                elif (word_to_guess[i] == guessed_letter):
                    temp += word_to_guess[i]
                else:
                    temp += '_'
            guessed_word = temp
        else:
            tries -= 1

        print(f"{guessed_word}\n")
        print(f"Lives remaining : {tries}")
        print(display_hangman(tries - 1))
        print()
        print("Used letters    :", *used_letter)

        if guessed_word == word_to_guess:
            print("\nYay! You guessed it.\n")
            break

    else:
        print("\nOhh no! Game Over.") 
        print(f"The word was \"{word_to_guess}\".\n") 

def display_hangman(tries):
    stages = ["""
                    --------
                    |      |
                    |      0
                    |     \\|/
                    |      |
                    |     / \\
                    -
              """,
              """
                    --------
                    |      |
                    |      0
                    |     \\|/
                    |      |
                    |     / 
                    -
              """,
              """
                    --------
                    |      |
                    |      0
                    |     \\|/
                    |      |
                    |    
                    -
              """,
              """
                    --------
                    |      |
                    |      0
                    |     \\|
                    |      |
                    |    
                    -
              """,
              """
                    --------
                    |      |
                    |      0
                    |      |
                    |      |
                    |    
                    -
              """,
              """
                    --------
                    |      |
                    |      0
                    |      
                    |      
                    |    
                    -
              """,
              """
                    --------
                    |      |
                    |      
                    |      
                    |      
                    |    
                    -
              """
              ]
    return stages[tries]

word = get_word()
play(word)
while input("Play Again? (Y/N): ").upper() == "Y":
    word = get_word()
    play(word)
