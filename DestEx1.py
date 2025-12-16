	
#Program for Demonstrating the Functionality of GC
#DestEx1.py
import time
class Employee:
	def __init__(self,eno,ename):
		print("I am from Parameterized Constructor:",id(self))
		self.eno=eno
		self.ename=ename
		print("\tEmployee Number=",self.eno)
		print("\tEmployee Name=",self.ename)
		print("-"*50)
	def __del__(self): # Destructor Def. called by GC
		print("\tGC Calls __del__()-For Dellocatin gthe Memory Space:",id(self))

#Main Program
print("Program Execution Started")
print("-----------------------------------------------")
eo1=Employee(10,"RS")
eo2=Employee(20,"DR")
eo3=Employee(30,"JH")
print("Program Execution Ended")
print("-----------------------------------------------")
time.sleep(5)	