class Dog():
	def __init__(self):
		self.__name='John'
		self.name='Jim'
	
	@property
	def name(self):
		return self.__name
		
	@name.setter
	def name(self,value):
		self.__name = value
	
	
	
	def dogname(self):
		return self.__name
		
		
if __name__=='__main__':
	dog = Dog()
	print(dog.name)
	print(dog.dogname())
	print(dog.name)
	dog.name='Joseph'
	print(dog.name)
	
