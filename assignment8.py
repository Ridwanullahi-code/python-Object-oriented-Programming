class Animal:

	species = "Canis familiaris"

	def __init__(self, Name, Age, Breed, Color,Sound, Fav_food ):

		self.Name = Name
		self.Age = Age
		self.Breed = Breed
		self.Color = Color 
		self.Sound = Sound
		self.Fav_food = Fav_food


	def Age(self):

		if self.Age == list(range(1,11)):
			return(f"{self.Name} you are a child")

		elif self.Age > 10:
			return(f'{self.Name} you are senior')

	def description(self):
		return f"{self.Name} is {self.Age} years old of  color {self.Color}"

	def speak(self):
		return f" {self.Name} says {self.Sound}"

	def favoriteFood(self):
		return f"{self.Name} eats {self.Fav_food}"

cat1 = Animal("bingo", 20, "jurry", "blue", "meaow", "meat")

print(cat1.Name, cat1.Age, cat1.Breed, cat1.Color, cat1.Sound, cat1.Fav_food)
print(cat1.description())
print(cat1.speak())
print(cat1.favoriteFood())


