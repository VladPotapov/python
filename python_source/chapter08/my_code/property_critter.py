class Critter(object):
    def __init__(self, name):
        print('na svet poyavilas zveryushka')
        self.name = name
    @property
    def name(self):
        return self.name