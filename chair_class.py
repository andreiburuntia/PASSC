#C = Cut seat
#F = Assemble feet
#B = Assemble backrest
#S = Assemble stabilizer bar
#P = Package chair

class Chair(object):
	def __init__(self, initial_components):
		self.components=initial_components #sequence of letters, one for each step, e.g.: CF = chair with seat and feet

	def has_cut_seat(self):
		if 'C' in self.components:
			return True
		else:
			return False

	def has_feet(self):
		if 'F' in self.components:
			return True
		else:
			return False

	def has_backrest(self):
		if 'B' in self.components:
			return True
		else:
			return False

	def has_stabilizer_bar(self):
		if 'S' in self.components:
			return True
		else:
			return False

	def has_packaging(self):
		if 'P' in self.components:
			return True
		else:
			return False

	def is_done(self):
		return (self.has_feet() and self.has_backrest() and self.has_stabilizer_bar() and self.has_cut_seat() and self.has_packaging())

	def has_none(self):
		if not self.components:
			return True

	def add_cut_seat(self):
		if not self.has_cut_seat():
			self.components+='C'

	def add_feet(self):
		if not self.has_feet():
			self.components+='F'

	def add_backrest(self):
		if not self.has_backrest():
			self.components+='B'

	def add_stabilizer_bar(self):
		if not self.has_stabilizer_bar():
			self.components+='S'

	def add_packaging(self):
		if not self.has_packaging():
			self.components+='P'

	def print_chair_components(self):
		print (self.components)

	def get_chair_components_chair_components(self):
		return self.components
