import chair_class
import abc
import sys, traceback
import time

# Interface


class Worker(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def try_get_chair(self, blackboard): pass

    @abc.abstractmethod
    def execute(self): pass

# Concrete class with implementations


class CWorker(Worker):

    def __init__(self):
        super(CWorker, self).__init__()

    def try_get_chair(self, blackboard):
    	pool=blackboard.get_chair_pool()
    	for chair in pool:
    		if not chair.has_cut_seat():
    			blackboard.give_chair(chair)
    			self.execute(chair)
    			blackboard.receive_chair(chair)

    def execute(self, chair):
        print('Executing Cut seat')
        time.sleep(1)
        chair.add_cut_seat()


class FWorker(Worker):

    def __init__(self):
        super(FWorker, self).__init__()

    def try_get_chair(self, blackboard):
    	pool=blackboard.get_chair_pool()
    	for chair in pool:
    		if not chair.has_feet():
    			blackboard.give_chair(chair)
    			self.execute(chair)
    			blackboard.receive_chair(chair)
    
    def execute(self, chair):
        print('Executing add Feet')
        time.sleep(1)
        chair.add_feet()


class BWorker(Worker):

    def __init__(self):
        super(BWorker, self).__init__()

    def try_get_chair(self, blackboard):
    	pool=blackboard.get_chair_pool()
    	for chair in pool:
    		if not chair.has_backrest():
    			blackboard.give_chair(chair)
    			self.execute(chair)
    			blackboard.receive_chair(chair)

    def execute(self, chair):
        print('Executing add Backrest')
        time.sleep(1)
        chair.add_backrest()


class SWorker(Worker):

    def __init__(self):
        super(SWorker, self).__init__()

    def try_get_chair(self, blackboard):
    	pool=blackboard.get_chair_pool()
    	for chair in pool:
    		if not chair.has_stabilizer_bar():
    			blackboard.give_chair(chair)
    			self.execute(chair)
    			blackboard.receive_chair(chair)

    def execute(self, chair):
        print('Executing add Stabilizer bar')
        time.sleep(1)
        chair.add_stabilizer_bar()


class PWorker(Worker):

    def __init__(self):
        super(PWorker, self).__init__()

    def try_get_chair(self, blackboard):
    	pool=blackboard.get_chair_pool()
    	for chair in pool:
    		if not chair.has_packaging():
    			blackboard.give_chair(chair)
    			self.execute(chair)
    			blackboard.receive_chair(chair)

    def execute(self, chair):
        print('Executing add Packaging')
        time.sleep(1)
        chair.add_packaging()

class Blackboard():

	def __init__(self,chairs):
		self.free_chairs=chairs
		self.chair_count=len(chairs)
		self.taken_chairs=[]
		self.finished_chairs=[]

	def get_chair_pool(self):
		return self.free_chairs;

	def give_chair(self, chair):
		self.free_chairs.remove(chair)
		self.taken_chairs.append(chair)

	def receive_chair(self, chair):
		if chair.is_done():
			self.finished_chairs.append(chair)
		else:
			self.free_chairs.append(chair)
		self.taken_chairs.remove(chair)
		if len(self.finished_chairs)==self.chair_count:
			print ("all chairs are done!")
			sys.exit()


c=CWorker()
f=FWorker()
b=BWorker()
s=SWorker()
p=PWorker()
chairs=[]
chair1=chair_class.Chair("")
chair2=chair_class.Chair("")
chairs.append(chair1)
chairs.append(chair2)
blackboard=Blackboard(chairs)

while True:
	c.try_get_chair(blackboard)
	f.try_get_chair(blackboard)
	b.try_get_chair(blackboard)
	s.try_get_chair(blackboard)
	p.try_get_chair(blackboard)