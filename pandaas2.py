#import pandas as pd
#print(pd.__version__)


class Basic:
    print("this is class")

    def display(self):
        a = 10
        b = 20

        print(a, b)


obj = Basic()
obj.display()

import pandas as pd

data= {
    "calories":[200,300,400],
    "Duration":[35,60,95]
}
dy = pd.DataFrame(data)
#print(dy.loc[[1,2]])
print(dy.head(2)) #prints top 2 rows
print(dy.tail(2)) #prints bottom 2 rows

src=pd.Series([0,1,2,3,4],index=['a','b','c','d','e'])
print(src)
print(src['a'])
print(src[::2])

