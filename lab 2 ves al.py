import random
from math import sin, radians

n = 20
a = [0] * n
x = 0
s=0
for i in range(len(a)):
    a[i] = random.randint(0, 360)
    print('A:', a)

for j in a:
    x = x + j

x_in_radians = radians(x)
s = sin(x_in_radians)
print("Sinüs değeri:", s)
