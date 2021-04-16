class Car:
	def __init__(self,name,car_color,model_year,speed,engine_capacity,mileage):
		self.name = name
		self.car_color = car_color
		self.model_year = model_year
		self.speed = speed
		self.engine_capacity = engine_capacity
		self.mileage = mileage

	def product_year(self):
		if self.model_year == 2021:
			return f"{self.name} :{self.model_year}"

	def car_speed(self):
		if self.speed ==  100:
			return f'{self.name} oh you have reach maximum speed'

		elif self.speed == 60:
			return f"{self.name} You are in normal speed" 

		else:
			return f"{self.name} increase your speed"

	def engine(self):
		if self.engine_capacity == 1000:
			return f"{self.name} has engine capacity: {self.engine_capacity}"
	
car1 = Car("Toyota", "Blue",2021,100,1000,12)
car2 =  Car("Camry", "White",2021,60,1000,16)
print(car1.name,car1.car_color,car1.model_year,car1.speed,car1.engine_capacity,car1.mileage)
print(car2.name,car2.car_color,car2.model_year,car2.speed,car2.engine_capacity,car2.mileage)
print(car1.car_speed())
print(car1.engine())
print(car2.car_speed())
print(car2.engine())








