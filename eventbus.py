from events import Events
import chair_class
import abc
import sys, traceback
import time

# Interface


class Worker(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def execute(self): pass

# Concrete class with implementations


class CWorker(Worker):

    def __init__(self):
        super(CWorker, self).__init__()

    def execute(self, chair):
        print('Executing Cut seat')
        time.sleep(1)
        chair.add_cut_seat()


class FWorker(Worker):

    def __init__(self):
        super(FWorker, self).__init__()
    
    def execute(self, chair):
        print('Executing add Feet')
        time.sleep(1)
        chair.add_feet()


class BWorker(Worker):

    def __init__(self):
        super(BWorker, self).__init__()

    def execute(self, chair):
        print('Executing add Backrest')
        time.sleep(1)
        chair.add_backrest()


class SWorker(Worker):

    def __init__(self):
        super(SWorker, self).__init__()

    def execute(self, chair):
        print('Executing add Stabilizer bar')
        time.sleep(1)
        chair.add_stabilizer_bar()


class PWorker(Worker):

    def __init__(self):
        super(PWorker, self).__init__()

    def execute(self, chair):
        print('Executing add Packaging')
        time.sleep(1)
        chair.add_packaging()

class EventBus():

	def __init__(self, chairs):
		self.chairs=chairs
		self.c=CWorker()
		self.f=FWorker()
		self.b=BWorker()
		self.s=SWorker()
		self.p=PWorker()
		self.events=Events()
		self.events.needs_cut_seat+=self.c.execute
		self.events.needs_feet+=self.f.execute
		self.events.needs_backrest+=self.b.execute
		self.events.needs_stabilizer_bar+=self.s.execute
		self.events.needs_packaging+=self.p.execute
	
	def needs_c(self, chair):
		if not chair.has_cut_seat():
			self.events.needs_cut_seat(chair)

	def needs_f(self, chair):
		if not chair.has_feet():
			self.events.needs_feet(chair)

	def needs_b(self, chair):
		if not chair.has_backrest():
			self.events.needs_backrest(chair)

	def needs_s(self, chair):
		if not chair.has_stabilizer_bar():
			self.events.needs_stabilizer_bar(chair)

	def needs_p(self, chair):
		if not chair.has_packaging():
			self.events.needs_packaging(chair)

	def start(self):
		while True:
			for chair in self.chairs:
				self.needs_c(chair)
				self.needs_f(chair)
				self.needs_b(chair)
				self.needs_s(chair)
				self.needs_p(chair)
				if chair.is_done():
					chairs.remove(chair)
				if len(chairs)==0:
					print ("all chairs are done!")
					sys.exit()



chairs=[]
chair1=chair_class.Chair("")
chair2=chair_class.Chair("")
chairs.append(chair1)
chairs.append(chair2)
eb=EventBus(chairs)
eb.start()