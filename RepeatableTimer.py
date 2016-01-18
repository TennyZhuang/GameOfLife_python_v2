from threading import Timer
from Subject import Subject


class RepeatableTimer(Subject):
    def __init__(self, interval):
        super().__init__()
        self.interval = interval

    def __del__(self):
        self.stop()

    def start(self):
        self.stop()
        self._timer = Timer(self.interval, self._run)
        self._timer.setDaemon(True)
        self._timer.start()

    def stop(self):
        if '_timer' in self.__dict__:
            self._timer.cancel()
            del self._timer

    def _run(self):
        self.notify()
        self.start()
