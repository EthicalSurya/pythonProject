import pickle

cars=['Audi','Benz','Ferrari','Alto']

f=open("cars.pkl",'wb')

pickle.dump(cars,f)

f.close()