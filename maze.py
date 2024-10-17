from cell import Cell
import time
import random

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

    def _create_cells(self):
        for i in range(self._num_cols):
            column = []
            self._cells.append(column)
            
            for j in range(self._num_rows):
                cell = Cell(self._win)
                column.append(cell)
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        
        x1 = i * self._cell_size_x + self._x1
        x2 = (i + 1) * self._cell_size_x + self._x1
        y1 = j * self._cell_size_y + self._y1
        y2 = (j + 1) * self._cell_size_y + self._y1

        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _break_entrance_and_exit(self):
        i = self._num_cols - 1
        j = self._num_rows - 1
        
        entrance = self._cells[0][0]
        exit = self._cells[i][j]

        entrance.has_top_wall = False
        exit.has_bottom_wall = False

        self._draw_cell(0, 0)
        self._draw_cell(i, j)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            next_index_list = []

            if i - 1 >= 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))

            if i + 1 < self._num_cols and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))

            if j - 1 >= 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))

            if j + 1 < self._num_rows and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return

            chosen_neighbor_indexes = random.randrange(len(next_index_list))
            i2 = next_index_list[chosen_neighbor_indexes][0]
            j2 = next_index_list[chosen_neighbor_indexes][1]

            if i2 > i:
                self._cells[i][j].has_right_wall = False
                self._cells[i2][j2].has_left_wall = False

            if i2 < i:
                self._cells[i][j].has_left_wall = False
                self._cells[i2][j2].has_right_wall = False

            if j2 > j:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i2][j2].has_top_wall = False

            if j2 < j:
                self._cells[i][j].has_top_wall = False
                self._cells[i2][j2].has_bottom_wall = False

            self._break_walls_r(i2, j2)

    def _animate(self):
        if self._win is None:
            return
        
        self._win.redraw()
        time.sleep(0.005)
