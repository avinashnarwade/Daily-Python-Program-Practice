# program for showing the internal flow of default thred --mainthread
# DefaultThreadInternalFlowEx.py

import threading
def welcome():
    print("\tLine-6:welcome() executed by:",threading.current_thread().name)
def hello():
    print("\tLine-8:hello() executed by:",threading.current_thread().name)
def hi():
    print("\tLine-10:hi() executed by:",threading.current_thread().name)
    
# main program 
print("Program execution started by:",threading.current_thread().name)
print("Main program line-14")
welcome()

print("Main program line-17")
hello()

print("Main program line-20")
hi()
print("program execution ended by:",threading.current_thread().name)
    