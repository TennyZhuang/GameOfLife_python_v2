from Subject import Subject


class Observer(object):
    def __init__(self, subject):
        assert isinstance(subject, Subject)
        self.subject = subject
        self.subject.attach(self)

    def __del__(self):
        if self in self.subject.observers:
            self.subject.detach(self)

    def update(self, **kwargs):
        raise NotImplementedError()
