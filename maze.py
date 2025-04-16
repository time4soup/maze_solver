from graphics import Line, Point

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
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__win = win
        self.center_point = Point(
            (x1 + x2) / 2, 
            (y1 + y2) / 2
        )
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
    
    def draw(self):
        if self.has_left_wall:
            self.__win.draw_line(
                Line(
                    Point(self.__x1, self.__y1),
                    Point(self.__x1, self.__y2)
                    )
                )
        if self.has_right_wall:
            self.__win.draw_line(
                Line(
                    Point(self.__x2, self.__y1),
                    Point(self.__x2, self.__y2)
                    )
                )
        if self.has_top_wall:
            self.__win.draw_line(
                Line(
                    Point(self.__x1, self.__y1),
                    Point(self.__x2, self.__y1)
                    )
                )
        if self.has_bottom_wall:
            self.__win.draw_line(
                Line(
                    Point(self.__x1, self.__y2),
                    Point(self.__x2, self.__y2)
                    )
                )

    def draw_move(self, to_cell, undo=False):
        fill_color = "red"
        if undo:
            fill_color = "gray"
        self.__win.draw_line(
            Line(self.center_point, to_cell.center_point), 
            fill_color
        )