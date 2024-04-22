import threading
import time
import os


def f(a:int):
    pool.acquire()
    try:
        print("Thread Started")
        time.sleep(a)
        print("Thread Finished")
    finally:
        pool.release()

pool = threading.BoundedSemaphore(value=2)

for i in range(5):
    threading.Thread(target=f,args=(20,)).start() 

while threading.active_count() != 1:
    print(threading.active_count())
    time.sleep(5)


print('ending')