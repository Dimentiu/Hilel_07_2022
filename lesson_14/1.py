from threading import Thread
from time import sleep

def msg_1():
    for i in range(5):
        print("Message 1")
        sleep(2)

def msg_2():
    while True:
        print("Message 2")
        sleep(2)

t1 = Thread(target=msg_1)
t2 = Thread(target=msg_2)

t1.start()
t2.start()

t1.join()
t2.join()

print("Hello")