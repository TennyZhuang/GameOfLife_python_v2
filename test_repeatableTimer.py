from unittest import TestCase
from RepeatableTimer import RepeatableTimer
from time import time, sleep
from math import fabs


class FakeRepeatableTimer(RepeatableTimer):
    def __init__(self, interval):
        super().__init__(interval)
        self.times = []

    def _run(self):
        self.times.append(time())
        super()._run()


class TestRepeatableTimer(TestCase):
    def setUp(self):
        self.timer = FakeRepeatableTimer(0.5)
        self.timer.start()


    def test_start(self):
        sleep(5)
        times = self.timer.times
        for i in range(len(times) - 1):
            self.assertTrue(fabs(times[i + 1] - times[i]) \
                            < 1.1 * self.timer.interval,
                            'Function should be called every interval')

    def test_stop(self):
        self.timer.stop()
        self.assertNotIn('_timer', self.timer.__dict__)
