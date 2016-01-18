from random import random
from Observer import Observer
from Subject import Subject


class Model(Observer, Subject):
    def __init__(self, subject, num_of_rows=20, num_of_cols=20, ratio=0.1):
        assert ratio >= 0 and ratio <= 1
        assert num_of_rows >= 0 and num_of_cols >= 0

        Observer.__init__(self, subject)
        Subject.__init__(self)
        self.num_of_rows = num_of_rows
        self.num_of_cols = num_of_cols
        self.round = 0
        self.map = [[1 if random() < ratio else 0 \
                     for _ in range(num_of_cols)] for _ in range(num_of_rows)]

    def update(self, **kwargs):
        backup = self.map_copy()

        for i in range(self.num_of_rows):
            for j in range(self.num_of_cols):
                num_of_neighbours = self.count_neighbours(i, j, backup)
                if num_of_neighbours == 3:
                    self.map[i][j] = 1
                elif num_of_neighbours != 2:
                    self.map[i][j] = 0

        self.round += 1

        self.notify(round=self.round, map=self.map)

    def map_copy(self):
        return [list(self.map[i]) for i in range(self.num_of_rows)]

    def count_neighbours(self, i, j, backup):
        dirs = [[1, 0, ], [0, 1, ],
                [-1, 0, ], [0, -1, ],
                [1, 1, ], [1, -1, ],
                [-1, 1, ], [-1, -1, ]]

        ans = 0
        for dir_ in dirs:
            ans += backup[(i + dir_[0]) % self.num_of_rows] \
                [(j + dir_[1]) % self.num_of_cols]

        return ans
