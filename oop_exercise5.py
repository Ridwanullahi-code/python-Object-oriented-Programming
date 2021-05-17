class Employee:

    firstName = None
    lastName  = None
    salary = 0
    raise_salary = 0

    def main(self):
        for _ in range(0,5):
            self.gefirstName()
            self.getLastName()
            self.getName()
            self.getID()
            self.getSalary()
            self.getAnnualSalary()
            self.raiseSalary()
            self.Employee_info()

    def getID(self):
        global id
        id = int(input("Enter the ID: "))
        return f'ID NO: {id}'

    def gefirstName(self):
        self.firstName =  input("Enter your first name: ")
        return f'FIRST NAME: {self.firstName}'

    def getLastName(self):
        self.lastName = str(input("Enter your last name: "))
        return f"LAST NAME: {self.lastName}"
    
    def getName(self):   
        return f'NAME: {self.firstName} {self.lastName}'

    def getSalary(self):
        self.salary = int(input("Salary: "))
        return f'SALARY: {self.salary}'

    def getAnnualSalary(self):
        global AnnualSalary
        AnnualSalary = self.salary * 12
        return f"Annual salary: {AnnualSalary}"

    def raiseSalary(self):
        self.raise_salary = self.raise_salary + self.salary * 100
        return f"{self.raise_salary}"

    def Employee_info(self):
        print(f'FIRST NAME: {self.firstName}')
        print(f"LAST NAME: {self.lastName}")
        print( f'NAME: {self.firstName} {self.lastName}')
        print(f'ID NO: {id}')     
        print(f'SALARY: {self.salary}')
        print( f"Annual salary: {AnnualSalary}")
        print(f"Percentage Salary: {self.raise_salary}")
       

Employee_account = Employee()   
print(Employee_account.main())
