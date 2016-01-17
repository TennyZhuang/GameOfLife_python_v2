import Observer

class Subject(object):
    def __init__(self):
        self.observers = []

    def attach(self, ob):
        assert isinstance(ob, Observer)
        self.observers.append(ob)

    def detach(self, ob):
        assert isinstance(ob, Observer)
        self.observers.remove(ob)

    def notify(self):
        for ob in self.observers:
            ob.update()
