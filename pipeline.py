# C = Cut seat
# F = Assemble feet
# B = Assemble backrest
# S = Assemble stabilizer bar
# P = Package chair

import chair_class
import time
import abc

# Interface


class Filter(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def execute(self): pass

# Concrete class with implementations


class CFilter(Filter):

    def __init__(self, chair):
        super(CFilter, self).__init__()
        self.data = chair

    def execute(self):
        print('Executing Cut seat')
        time.sleep(1)
        self.data.add_cut_seat()


class FFilter(Filter):

    def __init__(self, chair):
        super(FFilter, self).__init__()
        self.data = chair

    def execute(self):
        print('Executing add Feet')
        time.sleep(1)
        self.data.add_feet()


class BFilter(Filter):

    def __init__(self, chair):
        super(BFilter, self).__init__()
        self.data = chair

    def execute(self):
        print('Executing add Backrest')
        time.sleep(1)
        self.data.add_backrest()


class SFilter(Filter):

    def __init__(self, chair):
        super(SFilter, self).__init__()
        self.data = chair

    def execute(self):
        print('Executing add Stabilizer bar')
        time.sleep(1)
        self.data.add_stabilizer_bar()


class PFilter(Filter):

    def __init__(self, chair):
        super(PFilter, self).__init__()
        self.data = chair

    def execute(self):
        print('Executing add Packaging')
        
        self.data.add_packaging()


class Pipeline():

    def __init__(self, chair):
        self.chair = chair
        self.c = CFilter(self.chair)
        self.f = FFilter(self.chair)
        self.b = BFilter(self.chair)
        self.s = SFilter(self.chair)
        self.p = PFilter(self.chair)

    def do_it(self):
        self.c.execute()
        self.f.execute()
        self.b.execute()
        self.s.execute()
        self.p.execute()

        self.chair.print_chair_components()
        if self.chair.is_done:
            print("done!")

chair = chair_class.Chair("")
pipeline = Pipeline(chair)
pipeline.do_it()
