from graphics import Window
from maze import *

def main():
    win = Window(1000, 1000)

    maze = Maze(50, 50, 10, 10, 50, 35, win)

    win.wait_for_close()

if __name__=="__main__":
    main()