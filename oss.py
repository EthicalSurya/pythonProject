import os

curdir=os.getcwd()
print(curdir)

os.mkdir('suryapy')
import time
time.sleep(2)

os.rmdir('suryapy','newfolder')
time.sleep(2)

