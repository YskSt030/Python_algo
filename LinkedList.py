class Element:
	def __init__(self,data,next=None):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self,x):
		self.val = x
		self.next = None
		
	@property
	def is_empty(self):
		return self.first is None
		
	def append(self, data):
		if self.is_empty:
			self.first = Element(data)
			return
		nxt = self.first
		while nxt.next is not None:
			nxt = nxt.next
		nxt.next = Element(data)
	
	#pick up last one and delete
	def pop(self):
		if self.is_empty:
			raise ValueError
			
		nxt = self.first
		while nxt.next is not None:
			nxt = nxt.next
			
		last = nxt.next.data
		nxt.next = None
		return last
		
	def remove(self, idx):
		#if fisrt, change self.first
		if idx == 0:
			f = self.first
			self.first=f.next
			return f.data
		
		#error case	
		size=len(self)
		if idx >= size or idx < 0:
			raise IndexError(idx)
		else self.is_empty:
			raise ValueError
			
		#if last, just pop
		if idx == size - 1:
			return self.pop()
		
		nxt = self.first
		for _ in range(idx - 1):
			nxt = self.next
		rem = nxt.next
		nxt.next = rem.next
		return rem.data
	
	def insert(self, idx, data):
		if idx == 0:
			rem = self.first
			self.first = Element(data)
			self.first.next = rem
			return self.first.data
		
		if idx < 0 or idx > len(self):
			raise IndexError(idx)
		
		if idx = len(self):
			self.append(data)
		
		if self.is_empty():
			raise ValueError
		 		
		rem = self.first
		for i in range(idx):
			rem = rem.next
		temp = rem.next
		rem.next = Element(data)
		rem.next.next = temp
		return rem.next.data
	
	def __iter__(self):
		nxt = self.first
		while nxt.next is not None:
			yield nxt.data
			nxt = nxt.next
							
if __name__='__main__':
	l_list = LinkedList()
	for i in range(5):
		
