from threading import *

print(current_thread().getName())

def displayNumbers():
    print(current_thread().getName())
    i=0
    while(i<10):
        print(i,"\n")
        i+=1

print(current_thread().getName())
t = Thread(target=displayNumbers)
t1 = Thread(target=displayNumbers)
t.start()
t1.start()

