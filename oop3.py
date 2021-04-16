class Human:
	def __init__(self,first, last, number):
		self.first = first
		self.last = last
		self.number = number

	@property
	def age(self):
		return self._age

	@age.setter
	def age(self, value):
		if value >= 0:
			self._age = value
		else:
			raise valueError("age can't be negative!")

	@property
	def full_name(self):
		return f'{self.first} {self.last}'

	@full_name.setter
	def full_name(self, name):
		self.first, self.last = name.split(" ")
	
		
ridwan = Human("ridwan", "olalekan", 20)
print(ridwan.first, ridwan.last, ridwan.number)
ridwan.number = 10
print(ridwan.number)
print(ridwan.full_name)
ridwan.full_name = "Tim Minchin"
print(ridwan.full_name)
		 

