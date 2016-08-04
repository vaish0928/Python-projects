class Dog(object):
	#attributes
		#class object attribute
	species = "mammal"
	def __init__(self, breed, size, color, name):
		
		self.breed = breed
		self.size = size
		self.color = color
		self.name = name
	
	#methods
	def bark(self):
		if self.size < 20:
			print ("woof")
		else:
			print("woof woof woof")


#create a new dog	
ellie = Dog("lab", 60, "golden", "ellie")
nala = Dog("yorkie", 10, "brown", "nala")
print(ellie.name) #variable_name.name
print(ellie.species)
print(ellie)
print (type(ellie))
ellie.bark() #methods always need parenthesis 
print(nala.color)
nala.bark()
