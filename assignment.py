import threading
import time
import os

import numpy as np
MAT_SIZE:int = 1000
NUM_THREADS = [1,2,3,4,5,6,7,8]
OPERATIONS = 100
CONST_MAT = np.random.randint(low = -1e9,high= 1e9,size = (MAT_SIZE,MAT_SIZE))
# it may vary for ipynb and py implementations
INITIAL_THREAD_COUNT = threading.active_count()

def MutliplyMat(const_mat):
    pool.aquire()
    try:
        rand_mat = np.random.randint(low = -1e9,high= 1e9,size = (MAT_SIZE,MAT_SIZE))
        ans = np.dot(const_mat,rand_mat)
    finally:
        pool.release()


for n in NUM_THREADS:
    print("starting test for ", n)
    pool = threading.BoundedSemaphore(value= n)
    multiplication_counter:int = 0
    while multiplication_counter != OPERATIONS:
        if pool._value!=0:
            threading.Thread(target=MutliplyMat,args=(CONST_MAT,))
            multiplication_counter+=1


        

