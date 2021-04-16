class Game:
	player_choice = int(input("Enter your choice "))

	def __init__(self,name,health,attack,heal):
		self.name = name
		self.health = health
		self.attack = attack
		self.heal = heal

	def player_action(self):

		print("Rock...")
		print("Paper...")
		print("Scissors")
		return ("--" * 7)
		

	def player_info(self):
		return f"{self.name} {self.health} {self.attack} {self.heal}"

	def attack(self):
		if player_choice == 1:
			self.health -= 10
			return f"{health}"


player1 = Game("Ajayi",100,12,10)
player2 = Game("Max", 100,12,10)
print(player1.player_action())
print(player1.player_info())
print(player2.attack())	