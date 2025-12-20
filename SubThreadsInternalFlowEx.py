# program for showing the internal flow of sub threads with default thread mainthread 
# SubThreadsInternalFlowEx.py

import threading 
def welcome():
    print("\tLine-6:welcome() executed by:",threading.current_thread().name)
    
def hello():
    print("\tLine-8:hellow() executed by:",threading.current_thread().name)
def hi():
    print("\tLine-10:hi() executed by:",threading.current_thread().name)
    
# main program 

print("program execution has stated:",threading.current_thread().name)

# create 3 sub threads
t1 = threading.Thread(target=welcome) #here t1 is an object of thread class and whose name is thread-1
t2 = threading.Thread(target=hello) #here t2 is an objet of thread class and whose name is thread-2
t3 = threading.Thread(target=hi) #here t3 is an object of thread class and whose name is thread-3

# dispatch the sub threads 

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("program execution ended by:",threading.current_thread().name)