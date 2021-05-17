# <------- EMPLOYEE OBJECT CREATED USING PYTHON CLASS KEYWORD ----->
class Employee:

# <------ THIS CODE DEFINE CLASS PROPERTIES -------->
    def __init__(self, firstName, lastName, salary, id):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary
        self.id = id

#<------- THIS CODE DEFINE THE CLASS METHOD  ----->  
# -------ALL THE BELOW CODES ARE CLASS METHODS ---->  
    def main(self): 
        self.getfirstName()
        self.getLastName()
        self.getName()
        self.getID()
        self.getSalary()
        self.getAnnualSalary()
        self.raiseSalary()
        return "FINISHED"


    def getfirstName(self):
        print(f'FIRST NAME: {self.firstName}')

    def getLastName(self):
        print(f'LAST NAME: {self.lastName}')

    def getName(self):
        print(f'Name: {self.firstName} {self.lastName}')

    def getID(self):        
        print(f'ID NO : {self.id}')

    def getSalary(self):
        print(f'SALARY: {self.salary}')

    def getAnnualSalary(self):
        print('ANNUAL SALARY:'+ str(self.salary * 20))

    def raiseSalary(self):
        print('NEW SALARY:'+ str(self.salary * 100))
  
# <-------This code create the instance of Employee class and assign it to Employee1 variable ---->

Employee1 = Employee("John Micheal", "Rose Marry", 20000, 23441)
print(Employee1.main())

# <------ This code create the instance of Employee class and assign it to Employee2 variable ----->
Employee2 = Employee("Ahmad", "Abdullahi", 10000, 55657)
print(Employee2.main())

# <------ This code create the instance of Employee class and assign it to Employee3 variable ----->
Employee3 = Employee("Ajayi", "Ridwanullahi", 30000, 76868)
print(Employee3.main())

# ___ This code create the instance of Employee class and assign it to Employee4 variable ____
Employee4 = Employee("Jose", "MArry", 40000, 99777)
print(Employee4.main())
