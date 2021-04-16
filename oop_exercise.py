class Vehicle:

	color = "white"

	def __init__(self, name,max_speed,mileage):
		self.name =  name
		self.max_speed = max_speed
		self.mileage = mileage

class Bus(Vehicle):
	pass

class Car(Vehicle):
	pass

school_bus1 = Bus("school volvo", 180, 12)
print(school_bus1.color, school_bus1.name, school_bus1.max_speed, school_bus1.mileage)

school_bus2 = Car("Audi Qs", 240,18)
print(school_bus2.color, school_bus2.name, school_bus2.max_speed, school_bus2.mileage)
print(type(school_bus2))



class Vehicle:
	def __init__(self,name,mileage,capacity):

		self.name = name
		self.mileage = mileage
		self.capacity = capacity

	def fare(self):
		return self.capacity *100

class Bus(Vehicle):
	pass
school_bus = Bus("school volvo", 12, 50)
print(f"Total Bus fare is: {school_bus.fare()}")


