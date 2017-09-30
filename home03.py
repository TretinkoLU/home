 import math

class Sphere:
	 def __init__(self, radius=1, xcord=0.0, zcord=0.0, ycord=0.0):
		 self.radius = radius
		 self.xcord = xcord
		 self.zcord = zcord
		 self.ycord = ycord
		 self.tup_cord = (xcord, zcord, ycord)

	 def get_volume(self):
	 	return 4 / 3 * math.pi * self.radius ** 3

	 def get_radius(self):
	 	return self.radius

	 def get_center(self):
	 	return self.tup_cord

	 def set_radius(self, r):
	 	self.radius = r

	 def set_center(self, x, z, y):
	 	self.tup_cord = (x, z, y)

	 def is_point_inside(self, x, z, y):
	 	if (self.xcord - x) * 2 + (self.zcord - z) * 2 + (self.ycord - y) * 2 < self.radius * 2:
	 		return True
	 	else:
	 		return False

s0 = Sphere(0.5)
print(s0.get_center())
print(s0.get_volume())
print(s0.is_point_inside(0, -1.5, 0))
s0.set_radius(1.6)
print(s0.is_point_inside(0, -1.5, 0))