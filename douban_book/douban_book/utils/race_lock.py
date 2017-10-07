import threading
import time

balance = 0
lock = threading.Lock()

def change_balance(n):
    global balance
    balance = balance + n
    balance = balance - n
'''
def run_thread(n):
    for i in range(100000):
        change_balance(n)
'''
def run_thread(n):
    for i in range(100000):
        try:
            lock.acquire()
            change_balance(n)
        finally:
            lock.release()

t1 = threading.Thread(target = run_thread, args = (5,) )
t2 = threading.Thread(target = run_thread, args = (5,) )
t1.start()
t2.start()
t1.join()
t2.join()
print (balance)