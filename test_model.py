from unittest import TestCase
from Model import Model
from Subject import Subject


class TestModel(TestCase):
    def setUp(self):
        self.subject = Subject()
        self.model = Model(self.subject, 4, 4, 0.5)
        self.model.map = [
            [1, 0, 0, 1],
            [0, 0, 1, 0],
            [1, 0, 1, 0],
            [0, 0, 1, 1],
        ]

    def test_map_copy(self):
        backup = self.model.map_copy()
        backup[0] = [0, 1, 1, 0]
        self.assertEqual(self.model.map[0],
                         [1, 0, 0, 1], 'Should not change after update backup')

        backup[0][1] = 1
        self.assertEqual(self.model.map[0][1],
                         0, 'Should not change after update backup')


    def test_count_neighbours(self):
        self.assertEqual(self.model.count_neighbours(1, 1, self.model.map_copy()),
                         4, 'Should return the correct number of neighbours')
        self.assertEqual(self.model.count_neighbours(0, 0, self.model.map_copy()),
                         2, 'Should return the correct number of neighbours')

    def test_update(self):
        self.model.update()
        self.assertEqual(self.model.round, 1, 'Should go to next round')
        self.assertEqual(self.model.map, [
            [1, 1, 0, 0],
            [1, 0, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 0],
        ], 'Should update map correctly')
