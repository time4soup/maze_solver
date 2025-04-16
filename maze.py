from graphics import Line, Point
from time import sleep

class Cell:
    def __init__(
            self, 
            x1,
            y1, 
            x2, 
            y2,
            win,
            has_left_wall = True,
            has_right_wall = True, 
            has_top_wall = True,
            has_bottom_wall = True
    ):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win
        self._center_point = Point(
            (x1 + x2) / 2, 
            (y1 + y2) / 2
        )
        self.visited = False
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
    
    def draw(self):
        fill_color = "white"
        if self.has_left_wall:
            fill_color = "black"
        self._win.draw_line(
            Line(
                Point(self._x1, self._y1),
                Point(self._x1, self._y2)
                ), 
            fill_color
            )
        fill_color = "white"
        if self.has_right_wall:
            fill_color = "black"
        self._win.draw_line(
            Line(
                Point(self._x2, self._y1),
                Point(self._x2, self._y2)
                ), 
            fill_color
            )
        fill_color = "white"
        if self.has_top_wall:
            fill_color = "black"
        self._win.draw_line(
            Line(
                Point(self._x1, self._y1),
                Point(self._x2, self._y1)
                ), 
            fill_color
            )
        fill_color = "white"
        if self.has_bottom_wall:
            fill_color = "black"
        self._win.draw_line(
            Line(
                Point(self._x1, self._y2),
                Point(self._x2, self._y2)
                ), 
            fill_color
            )

    def draw_move(self, to_cell, undo=False):
        fill_color = "red"
        if undo:
            fill_color = "gray"
        self._win.draw_line(
            Line(self._center_point, to_cell._center_point), 
            fill_color
        )

class Maze:
    def __init__(
            self, 
            x1, 
            y1, 
            num_rows, 
            num_cols, 
            cell_size_x, 
            cell_size_y, 
            win=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []

        self._create_cells()
    
    def _create_cells(self):
        dx = self._cell_size_x
        dy = self._cell_size_y
        x1 = self._x1
        y1 = self._y1
        for i in range(0, self._num_cols):
            cell_col = []
            for j in range(0, self._num_rows):
                cell_x1 = (x1 + i*dx)
                cell_y1 = (y1 + j*dy)
                cell_col.append(Cell(cell_x1, cell_y1, cell_x1 + dx, cell_y1 + dy, self._win))
            self._cells.append(cell_col)

        self._break_entrance_and_exit()
        
        for col in self._cells:
            for cell in col:
                self._draw_cell(cell)
    
    def _draw_cell(self, cell):
        if self._win == None:
            return
        cell.draw()
        self._animate()
    
    def _animate(self):
        if self._win == None:
            return
        self._win.redraw()
        sleep(0.05)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
    
    def _break_wall_r(self, i, j):
        neighbor_left, neighbor_right, neighbor_top, neighbor_bottom = self._get_neighbors(i, j)
        if (neighbor_left is None) and (neighbor_right is None) and (neighbor_top is None) and (neighbor_bottom is None):
            return
        # make recursive
    
    def _get_neighbors(self, i, j):
        if i == 0:
            neighbor_left = None
        else:
            neighbor_left = (i - 1, j)
        if i == (self._num_cols - 1):
            neighbor_right = None
        else:
            neighbor_right = (i + 1, j)
        if i == 0:
            neighbor_top = None
        else:
            neighbor_top = (i, j - 1)
        if i == (self._num_rows - 1):
            neighbor_bottom = None
        else:
            neighbor_bottom = (i, j + 1)
        return neighbor_left, neighbor_right, neighbor_top, neighbor_bottom
