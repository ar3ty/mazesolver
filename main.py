from graphics import Window
from maze import *
from config import *

def main():
    
    win = Window()
    win.wait_for_close()
    
    maze = Maze(win.input['Margin'],
                win.input['Margin'], 
                win.input['Number of columns'], 
                win.input['Number of rows'], 
                win.input['Cell width'], 
                win.input['Cell height'],
                win)
    
    win.wait_for_close()

    ##is_solved = maze.solve()
    ##if is_solved:
        ##print("maze is solved")
    ##else:
        ##print("maze is not solved, smth is wrong")

   

if __name__=="__main__":
    main()