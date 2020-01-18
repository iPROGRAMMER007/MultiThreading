from threading import *

class MyThread:

    def displayNumber(self):
        i=0
        print(current_thread().getName())
        while(i<=10):
            print(i)
            i+=1

    def addition(self):
        print(current_thread().getName())
        a = 10
        b = 20
        print(a+b)


print(current_thread().getName())
obj = MyThread()
t1 = Thread(target=obj.addition)
t1.start()
t = Thread(target=obj.displayNumber)
t.start()

