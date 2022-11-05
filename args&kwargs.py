def myfun(normal,*devs,**roles):
    print(normal)
    for info in devs:
        print(info)
    print("\nTheir roles are:")
    for key,value in roles.items():
        print(f"{key} on {value} band")


dev = ['Surya', 'Anil', 'Sharwa','Anand']
normal = "The students are:"
rol={"Systems Engineer":"C1", "IT Analyst":"C2", "Trainee":"y", "Lead":"L1"}

myfun(normal,*dev,**rol)


def customer(name,*arg):   #args
    print('\n',name)
    print(arg)

customer('Surya',27,9494233195,"Hyd")  #kwargs

def customers(name,**kwargs):
    print('\n',name)
    for i,j in kwargs.items():
        print(i,j)

customers('Surya',age=27,mob=9494233195,city="Hyd")