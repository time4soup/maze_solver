from graphics import Window, Line, Point
from maze import Cell, Maze

def main():
    win = Window(400, 600)
    # c1 = Cell(100, 100, 200, 200, win)
    # c1.draw()
    # c2 = Cell(220, 100, 320, 200, win)
    # c2.has_bottom_wall = False
    # c2.has_top_wall = False
    # c2.draw()
    # c3 = Cell(340, 100, 440, 200, win)
    # c3.has_left_wall = False
    # c3.has_right_wall = False
    # c3.draw()
    # c4 = Cell(100, 220, 200, 320, win)
    # c4.has_top_wall = False
    # c4.has_left_wall = False
    # c4.has_right_wall = False
    # c4.draw()
    # c1.draw_move(c2)
    # c2.draw_move(c3)
    # c3.draw_move(c4, undo=True)

    m = Maze(10, 10, 5, 4, 20, 20, win, seed=1)
    print(f"Maze solved: {m.solve()}")
    win.wait_for_close()

main()