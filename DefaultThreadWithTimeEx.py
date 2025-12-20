# program for showing  the internal flow of default thread with time 
# DefaultThreadWithTimeEx.py 

import threading,time

def squares(lst):
    for val in lst:
        print("\t{}----->({}) = {}".format(threading.current_thread().name,val,val**2))
        time.sleep(1)

def cubes(lst):
    for val in lst:
        print("\t{}-------->Cube({})={}".format(threading.current_thread().name,val,val**3))
        time.sleep(1) 

# main program 
bt = time.time()
print("Program execution started by:",threading.current_thread().name)
lst = [12,19,4,-9,15,25,13,16,28]
squares(lst) #function call
print("-----------------------------")

cubes(lst) #function call 
print("program execution ended by:",threading.current_thread().name)
et = time.time()
print("default thread totall execution time = ",(et-bt))

        