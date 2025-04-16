from tkinter import BOTH, Canvas, Tk

class Window:
    def __init__(self, height, width):
        self._root = Tk()
        self._root.title = ("Maze Solver")
        self._root.protocol("WM_DELETE_WINDOW", self.close)
        self._canvas = Canvas(height=height, width=width)
        self._canvas.pack()
        self._running = False
    
    def redraw(self):
        self._root.update()
        self._root.update_idletasks()

    def wait_for_close(self):
        self._running = True
        while self._running == True:
            self.redraw()
    
    def close(self):
        self._running = False
    
    def draw_line(self, line, fill_color="black"):
        line.draw(self._canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self._p1 = p1
        self._p2 = p2
    
    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self._p1.x, self._p1.y, self._p2.x, self._p2.y, fill=fill_color, width=2
        )