class Circle(object):
	pi = 3.14
	def __init__(self, radius):
		self.radius = radius
		
		
	def area(self):
		area = self.pi* self.radius ** 2
		return area
		
		
	def circumference(self):
		circ = 2 * self.pi * self.radius
		return circ
		
big_circle = Circle(10)
area_1 = big_circle.area()
circ_1 = big_circle.circumference()

print(area_1)
print(circ_1)