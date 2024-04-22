import threading
import time
import os

def f(a:int):
    print("Thread Started")
    for i in range(a):
        print(os.getpid())
        time.sleep(1)
    print("Thread Finished")

threads = []
for _ in range(4):
    ref = threading.Thread(target=f,args=(20,)) 
    threads.append(ref)

print(threading.active_count())
for i in threads:
    i.start()
print('my code is running')
print("hello")
print(threading.active_count())
# for i in threads:
#     i.join()
while threading.active_count() !=1:
    print('womp womp')
    time.sleep(5)
# print(threading.active_count())

