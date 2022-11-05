ls=['bhendi','aloo','chopstick','chowmein']
# i=1
# for item in ls:
#     if i%2!=0:
#         print(item)
#     i+=1

for index,item in enumerate(ls):
    if index%2==0:
        print(f"jarvis please buy {item}")


