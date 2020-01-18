from threading import *

class BookMyBus:

   

    def buy(self):
        print(current_thread().getName())
        print("Confirming a seat")
        print("Processing the payment")
        print("Printing the ticket")


obj = BookMyBus()

t1 = Thread(target=obj.buy)
t2 = Thread(target=obj.buy)
t3 = Thread(target=obj.buy)

t1.start()
t2.start()
t3.start()
