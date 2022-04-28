import matplotlib.pyplot as plt
#%matplotlib inline

# create classes
class Circle(object):
	# constructor with default
	def __init__(self, radius, color='green'):
		self.radius = radius
		self.color = color

	# method to increase size
	def increase_radius(self, r):
		self.radius = self.radius + r
		return (self.radius)

	# draw method
	def drawCircle(self):
		plt.gca().add_patch(plt.Circle((0,0), radius=self.radius, fc=self.color))
		plt.axis('scaled')
		plt.show(block=True)

class Rectangle(object):
	# constructor with defaults
	def __init__(self, width=2, height=3, color='red'):
		self.width = width
		self.height = height
		self.color = color

	# draw method
	def drawRectangle(self):
		plt.gca().add_patch(plt.Rectangle((0,0), self.width, self.height, fc=self.color))
		plt.axis('scaled')
		plt.show(block=True)


## test classes
RedCircle = Circle(10, 'red')
RedCircle.drawCircle()

# change radius with method
print "Object radius:", RedCircle.radius
RedCircle.increase_radius(2)
print "Object radius after increment:", RedCircle.radius
RedCircle.drawCircle()

# new object with deafult color
GreenCircle = Circle(100)
print "Radius:", GreenCircle.radius
print "Color:",GreenCircle.color
GreenCircle.drawCircle()

BlueRectangle = Rectangle(2, 3, 'Blue')
BlueRectangle.drawRectangle()

# check attributes
print "Rectangle specifications:", BlueRectangle.height, BlueRectangle.width









