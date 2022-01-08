from random import *
import os




def hangman(list): # has the 6 
    state = len(list)

    if state == 0:
        print("""
                 ____
                |    |
                     |
                     |
                     |
                  ___|____     
                """)

    elif state == 1:
        print("""
                 ____
                |    |
                O    |
                     |
                     |
                  ___|____     
                """)

    elif state == 2:
        print("""
                 ____
                |    |
                O    |
                |    |
                     |
                  ___|____     
                """)

    elif state == 3:
        print("""
                 ____
                |    |
                O    |
                |-   |
                     |
                  ___|____     
                """)
    elif state == 4:
        print("""
                 ____
                |    |
                O    |
               -|-   |
                     |
                  ___|____     
                """)
    elif state == 5:
        print("""
                 ____
                |    |
                O    |
               -|-   |
                 \   |
                  ___|____     
                """)
    elif state == 6:
        print("""
                 ____
                |    |
                O    |
               -|-   |
               / \   |
                  ___|____     
                """)
        print("You lose")


def replace(originalList,newList, choice):
    if choice in originalList:
        for i in range(len(originalList)):
            if originalList[i] == choice:
                newList[i] = originalList[i]

def hangmanGame():
    lettersGuessed = []
    gameOn = True
    words = ["orange", "banana", "strawberry"] # avaliable words, if you want to add custom ones, simply add a new item as a string
    lettersGuessed.clear()
    while gameOn:
        try:
            wordList = list(word)
                
        except NameError:
            word = words[randint(0,len(words) - 1)] 
            wordList = list(word)
            maskedList = []
            [maskedList.append("_") for x in wordList] # creates the underscores based on how many letters there are in the word

        print(" ".join(maskedList))
        print(lettersGuessed)
        pGuess = input("What is your guess? >> ")

        
        if pGuess in wordList:
            replace(wordList, maskedList, pGuess)

        

        elif pGuess not in wordList:
            lettersGuessed.append(pGuess)
            os.system('cls' if os.name == 'nt' else 'clear')
            hangman(lettersGuessed)

        if len(lettersGuessed) == 6:
            gameOn = False
            startOver = input("Would you like to play again? (y/n) >>> ")

            if startOver == "y":
                hangmanGame()
            else:
                print("Thanks for playing!")

hangmanGame()
    
    
    
    

