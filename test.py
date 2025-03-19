import unittest
from maze import *

class MazeTests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_cols, num_rows, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_create_cells2(self):
        num_cols = 6
        num_rows = 12
        m1 = Maze(0, 0, num_cols, num_rows, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_create_cells3(self):
        num_cols = 20
        num_rows = 16
        m1 = Maze(0, 0, num_cols, num_rows, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_cols, num_rows, 10, 10)
        self.assertEqual(m1._cells[0][0].has_top_wall, False)
        self.assertEqual(m1._cells[m1._num_cols - 1][m1._num_rows - 1].has_bottom_wall, False)   

    def test_reset_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_cols, num_rows, 10, 10)
        for i in range(num_cols):
            for j in range(num_rows):
                self.assertEqual(m1._cells[i][j].visited, False)

if __name__ == "__main__":
    unittest.main()