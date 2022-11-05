import pickle

f=open("cars.pkl",'rb')

b=pickle.load(f)
print(b)

f.close()