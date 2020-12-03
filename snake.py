# Snake game written in Python by Are Oelsner
import tkinter as tk
class Constants:
    WIDTH = 30#0
    HEIGHT = 30#0
    DELAY = 100
    #DOT_SIZE = 10
    #OPEN_SPACES = 27
class Snake:
    length = 1
    # x position of snake head on board
    # y position of snake head on board
    # maybe have snake just store head and have the rest be controlled by the board?
    # length of snake

class Board:
    length = 10
    width = 10

class Game:
    # Class Variables
    time = 0 # maybe don't need to store this, could use while loop
    score = 0
    board = Board()
    snake = Snake()


window = tk.Tk()
window.title("Snake")
score = 5
lblInst = tk.Label(window, text = ("Try to eat as much fruit as you can!",  score))


lblInst.grid(row=0, column=0, columnspan=5)

window.mainloop()