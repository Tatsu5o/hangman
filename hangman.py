from email import charset
from ntpath import join
from tkinter import HORIZONTAL
from tkinter.tix import Tree


def hangman(word):
    wrong = 0
    stages = ["",
              "__________          ",
              "|                   ",
              "|         |         ",
              "|         0         ",
              "|        /|¥        ",
              "|        / |        ",
              "|                   "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
            print("¥n")
            msg = "Please guess 1 word"
            char = input(msg)
            if char in rletters:
                cind = rletters.index(char)
                board[cind] = char
                rletters[cind] = '$'
            else:
                wrong += 1
            print("".join(board))
            e = wrong + 1
            print("¥n".join(stages[0:e]))
            if "_" not in board:
                print("You Win!")
                print(" ".join(board))
                win = True
                break
            if not win:
                print("¥n".join(stages[0:wrong+1]))
                print("You lose! Answer is {}.".format(word))
