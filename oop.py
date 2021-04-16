class BankAccount:
	def __init__(self,AccName,AccNumber,AccType,Amount):
		self.AccName = AccName
		self.AccNumber = AccNumber
		self.AccType = AccType
		self.Amount = Amount

	def Withdraw(self):
		return f"{self.AccName} Withdraw {self.Amount} Today"

	def Deposite(self):
		return f"{self.AccName} Deposite {self.Amount} Yesterday"

	def CheckBalance(self):
		return f"{self.AccName} Account Balance remain {self.Amount}"

	def CreateAcct(self):
		return f'{self.AccName} Account was successfully created'
	
	def Account_balance(self, widthraw):
		user_action = input("Do you want to widthraw y/n ").upper()
		self.Widthraw = widthraw
		if user_action == "Yes":
			self.Amount  -= self.Widthraw
			print(f'Your account balance is: {self.Amount}')


customer = BankAccount("AJAYI",3424792409,"Saving", 5000)
print(customer.AccName,customer.AccNumber,customer.AccType,customer.Amount)
print(customer.Withdraw())
print(customer.Deposite())
print(customer.CheckBalance())
print(customer.CreateAcct())
print(customer.Account_balance(1000))
#print(customer.Account_balance(int(input('Enter amount to widthraw '))))


