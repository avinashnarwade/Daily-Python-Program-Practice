# program for showing the internal flow of sub threads with time 
# SubThreadsWithTimeEx.py

import threading,time

def squares(lst):
    for val in lst:
        print("\t{}------>square({})={}".format(threading.current_thread().name,val,val**2))
        time.sleep(1)
        
def cubes(lst):
    for val in lst:
        print("\t {}-------------->cube({})={}".format(threading.current_thread().name,val,val**3))
        time.sleep(1)
        
# main program 
bt = time.time()
print("Program execution has been started:",threading.current_thread().name)
lst =[12,19,4,-9,15,25,13,16,28]
# creat 2 sub threads

t1 = threading.Thread(target=squares,args=(lst,))
t1.name = "RS"

t2 = threading.Thread(target=cubes,args=(lst,))  
t2.name=("DR")

#dispatch the sub threads

t1.start()
t2.start()

t1.join()
t2.join()

print("Program execution ended by:",threading.current_thread().name)
et = time.time()
print("Sub threads total execution time = ",(et-bt))   