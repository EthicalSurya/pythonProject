class student:
    school='RPHS'  #Class Variable
    def __init__(self,m1,m2,m3):
        self.m1 = m1      #Instance variabless
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def info(cls):
        return cls.school


s1=student(22,35,75)
s2=student(55,24,36)

print(s2.avg())
print(student.info())


#----------Achieving Method Overloading----------------
class pupil:

    def  sum(self,a=None,b=None,c=None):

        if a!=None and b!=None and c!=None:
           return a + b + c
        elif a!=None and b!=None:
            return a+b
        else:
            return a


p=pupil()
print(p.sum(7,5,6))

