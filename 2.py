import math
a = int(input("What is a?"))
b = int(input("What is b?"))
c = int(input("What is c?"))


b = b**2-4*a*c
if d < 0:
	print(str("No solution, D < 0"))
elif d == 0:
	x = (-d + math.sqrt(d))/2*a
	print(str("D = 0; X = ") , x)
else:
	x1 = (-d + math.sqrt(d))/2*a
	x2 = (-d - math.sqrt(d))/2*a
	print(str("D = "), d, str ("; X1 = "), x1, str("; X2 = "), x2)