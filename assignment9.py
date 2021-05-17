class User:
	active_users = 0

	def __init__(self, first, last, thing, age, state, town, address):
		self.first = first
		self.last = last
		self.thing = thing
		self.age = age
		self.state = state
		self.town = town
		self.address = address
		User.active_users +=1

	def full_name(self):
		return f"{self.first} {self.last}"

	def initials(self):
		return f"{self.first[0]} and {self.last[0]}"

	def likes(self):
		return f"{self.first} likes {self.thing}"

	def is_senior(self):
		return self.age >= 65 

	def birthday(self):
		self.age = + 1
		return f" Happy {self.age}th, {self.first}"

	def user_state(self):
		return f"{self.first} {self.last} is from {self.state}"

	def user_town(self):
		return f"{self.first} {self.last} from {self.state} is living in {self.town}"

	def user_address(self):
		return f"{self.first} {self.last} Of NO 24 {self.address} compound "

print("User: " + str(User.active_users))
user1 = User("ajayi", "ridwan", "pawpaw", 20, "Osun", "Ileogbo", "Omoforilu" )
user2 = User("akande", "ismail", "pawpaw", 23, "Osun", "Oshogbo", "Ailara" )
print("User: " + str(User.active_users))
print(user1.first, user1.last, user1.age, user1.state, user1.town, user1.address)
print("---"*16)
print(user1.full_name())
print("---"*16)
print(user1.initials())
print("---"*16)
print(user1.likes())
print("---"*16)
print(user1.birthday())
print("---"*16)
print(user1.user_state())
print("---"*16)
print(user1.user_town())
print("---"*16)
print(user1.user_address())
print("---"*16)
print(user2.first, user2.last, user2.age, user2.state, user2.town, user2.address)
print("---"*16)
print(user2.full_name())
print("---"*16)
print(user2.initials())
print("---"*16)
print(user2.likes())
print("---"*16)
print(user2.birthday())
print("---"*16)
print(user2.user_state())
print("---"*16)
print(user2.user_town())
print("---"*16)
print(user2.user_address())
print("---"*16)



