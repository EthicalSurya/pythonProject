class Employee:
    company="TCS"
    salary=1000
    loc="hyd"
    
    @classmethod
    def increment(cls,sal):
        cls.salary=sal

e=Employee()
print(e.salary)
e.increment(2000)
print(e.salary)
print(Employee.salary)
