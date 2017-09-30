a = [1,2,3,4,5]
c = 0
d = 0
for x in a:
    b = a[0] + a[2] + a[4]
    c += b
c * a[4]
d += c
print(d)
