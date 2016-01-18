class Subject(object):
    def __init__(self):
        self.observers = []

    def attach(self, ob):
        self.observers.append(ob)

    def detach(self, ob):
        self.observers.remove(ob)

    def notify(self, **kwargs):
        for ob in self.observers:
            ob.update(**kwargs)
