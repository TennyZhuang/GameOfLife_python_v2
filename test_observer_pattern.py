from unittest import TestCase, mock
from Subject import Subject
from Observer import Observer


class TestObserverPattern(TestCase):
    def setUp(self):
        self.subject = Subject()
        self.observers = [Observer(self.subject) for _ in range(3)]

    def test_attach(self):
        ob4 = Observer(self.subject)
        self.subject.attach(ob4)
        self.assertEqual(self.subject.observers[-1],
                         ob4, 'Should append new observer')

    def test_detach(self):
        ob2 = self.subject.observers[1]
        self.subject.detach(ob2)
        self.assertNotIn(ob2, self.subject.observers,
                         'Should detach observer')

    def test_notify(self):
        with mock.patch('Observer.Observer.update') as mock_update:
            try:
                self.subject.notify()
            except NotImplementedError:
                pass

            mock_update.assert_has_calls([mock.call() for _ in range(3)])
