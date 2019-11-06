import random

class Stack:
	def __init__(self):
		self.top = None
		self.min = None
	
	def Push(self, num_):
		if self.top is None:
			self.top = StackNode(num_)
			self.min = num_
		else:
			T = self.top
			self.next = T
			self.top = StackNode(num_)
			if self.min > num_:
				self.min = num_
				
	def Pop(self):
		T = self.top
		self.top = T.next
		return T.data
		
	def Peek(self):
		return self.top.data
		
	def IsEmpty(self):
		return self.top is None
	
	# Question 3.2 of Cracking coding interview
	# return the minumum number with O(1)
	def Min(self):
		return self.min
		
		
class StackNode:
	def __init__(self, num_):
		self.data = num_
		self.next = None
		
		
if __name__ == '__main__':
	stack = Stack()
	NUMOFLEN = 10
	for i in range(NUMOFLEN):
		num_ = random.randint(1, 100)
		print('Input num: '+str(num_))
		stack.Push(num_)
		
	print(stack.Peek())
		

