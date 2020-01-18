from threading import *
from time import *

class Producer:
    def __init__(self):
        self.products = []
        self.orderplaced = False

    def produce(self):
        print(current_thread().getName())
        for i in range(1,5):
          #  print(current_thread().getName())
            self.products.append("Products"+str(i))
            sleep(1)
            print("Item added")
        self.orderplaced = True


class Consumer:
    def __init__(self,prod):
        self.prod = prod

    def consume(self):
        print(current_thread().getName())
        while self.prod.orderplaced == False:
           # print(current_thread().getName())
            print("Waiting for the orders")
            sleep(0.5)

        print("Order shipped ",self.prod.products)


p = Producer()
c = Consumer(p)

t1 = Thread(target=p.produce)
t2 = Thread(target=c.consume)

t1.start()
t2.start()






