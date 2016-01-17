import Subject

class Observer(object):
    def __init__(self, subject):
        assert isinstance(subject, Subject)
        self.subject = subject

    def update(self):
        raise NotImplementedError()
