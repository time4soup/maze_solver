import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells1(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_create_cells2(self):
        num_cols = 100
        num_rows = 20
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_break_entrance_and_exit(self):
        m = Maze(0, 0, 10, 20, 10, 10)
        self.assertFalse(
            m._cells[0][0].has_top_wall
        )
        self.assertFalse(
            m._cells[m._num_cols - 1][m._num_rows - 1].has_bottom_wall
        )

if __name__ == "__main__":
    unittest.main()