from threading import *
from time import *

class Producer:
    def __init__(self):
        self.products = []
        self.c = Condition()

    def produce(self):
        self.c.acquire()
        print(current_thread().getName())
        for i in range(1,5):
          #  print(current_thread().getName())
            self.products.append("Products"+str(i))
            sleep(1)
            print("Item added")
        self.c.notify()
        self.c.release()



class Consumer:
    def __init__(self,prod):
        self.prod = prod

    def consume(self):
        print(current_thread().getName())
        self.prod.c.acquire()
        self.prod.c.wait(timeout=0)
        self.prod.c.release()
        print("Order shipped ",self.prod.products)


p = Producer()
c = Consumer(p)

t1 = Thread(target=p.produce)
t2 = Thread(target=c.consume)

t1.start()
t2.start()






