class Employee:
    company="Google" #class attribute
    def get_sal(self,sign):
        print(f"Salary of the employee working in {self.company} is {self.salary}\n {sign}")

    @staticmethod  #decorator which is used without self parameter/arg
    def greet():
        print(f"Hi user @ {Employee.company}")

harry=Employee() #1st instance
harry.salary=10000 #instance attribute
# Employee.company="YouTube"   #Changing the class attribute value
harry.get_sal("ThankYou!")

Employee.greet() #static method called with class name
# harry.greet() # static method called with instance name

rajini=Employee() #2nd instance
rajini.salary=15000
rajini.get_sal("Thanks!")
rajini.greet()


