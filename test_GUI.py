from unittest import TestCase, mock
from GUI import GUI
from Subject import Subject
from RepeatableTimer import RepeatableTimer
from tkinter import *


class FakeGUI(GUI):
    def __init__(self, subject, timer):
        Tk.mainloop = lambda _: None
        super().__init__(subject, timer)


class TestGUI(TestCase):
    def setUp(self):
        self.timer = RepeatableTimer(0.3)
        self.gui = FakeGUI(Subject(), self.timer)

    def tearDown(self):
        self.timer.stop()

    def test_start_button_onclick(self):
        with mock.patch('RepeatableTimer.RepeatableTimer.start') as mock_start:
            self.gui.start_button_onclick()
            self.assertEqual(self.gui.start_button['state'],
                             'disabled', 'button should be disabled')
            mock_start.assert_called_once_with()

    def test_update(self):
        self.gui.update(round=3, map=[[1]])
        label_text = self.gui.round_label['text']
        round_now = int(label_text[(label_text.index(':') + 1)])
        self.assertEqual(round_now, 3, 'Should update round')

    def test_draw(self):
        with mock.patch('tkinter.Canvas.create_rectangle') as mock_create_rectangle:
            self.gui.draw([
                [1, 0, 1, 1],
                [0, 0, 1, 1],
                [0, 1, 1, 1],
                [0, 0, 0, 1],
            ])

            calls = [mock.call(0, 0, 360.0, 360.0, outline='white', fill='white')]

            calls_pos = [
                [0, 0, 89, 89],
                [180, 0, 269, 89],
                [270, 0, 359, 89],
                [180, 90, 269, 179],
                [270, 90, 359, 179],
                [90, 180, 179, 269],
                [180, 180, 269, 269],
                [270, 180, 359, 269],
                [270, 270, 359, 359],
            ]

            calls += list(map(lambda x: mock.call(*x, outline='white', fill='black'),
                              calls_pos))

            mock_create_rectangle.assert_has_calls(calls)
