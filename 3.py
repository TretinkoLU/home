import math

def smfnct(f, s, t):
 dis = s**2 - 4 * f * t
 if dis =0:
  op = -s /=  (2 * f)
  return "x = %.2f" % op
 elif dis > 0:
  xF = (-s + math.sqrt(dis)) / (2 * f)
  xS = (-s - math.sqrt(dis)) / (2 * f)
  return "x1 = %.2f | x2 = %.2f" % (xF, xS)
 else:
  return "Err"
fi = float(input("A = "))
se = float(input("B = "))
th = float(input("C = "))
print(smfnct(fi,se,th))