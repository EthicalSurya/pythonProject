class Employee:
    company = "TCS"
    salary = 5000
    bonus= 500
    # totalsal= 5500


    ''' @property is a "Getter" used as a property of a class though it's a function()
    we can call 'e.totalsal' instead of 'e.totalsal()' '''

    @property
    def totalsal(self):
        return self.salary + self.bonus

    @totalsal.setter #setting bonus val according to the totalsal given as parameter
    def totalsal(self,total):
        self.bonus=total-self.salary

e=Employee()
print(e.totalsal)

e.totalsal=6000 #making total sal to 6000
print(e.salary)
print(e.bonus)

