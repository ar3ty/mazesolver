from graphics import Window
from maze import Cell

def main():
    win = Window(800, 600)

    cell1 = Cell(win)
    cell2 = Cell(win)
    cell3 = Cell(win)
    cell1.draw(100, 100, 200, 200)
    cell2.draw(200, 100, 300, 200)
    cell1.draw_move(cell2)
    cell3.draw(300, 100, 400, 200)
    cell2.draw_move(cell3, True)

    win.wait_for_close()

if __name__=="__main__":
    main()