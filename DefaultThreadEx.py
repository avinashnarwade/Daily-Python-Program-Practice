# program for showing the default thred
# DefaultThreadEx.py

# import threading 
# tname = threading.current_thread().name
# print("Default thred name: ",tname)
# print("By default Number of Threads in python Program = ",
#       threading.active_count())



import threading
tname = threading.current_thread().name
print("Default thred name = ",tname)
print("By default number of thread in python program = ",
      threading.active_count())