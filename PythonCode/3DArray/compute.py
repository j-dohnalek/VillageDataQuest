from numpy import genfromtxt

x, y, z = 10, 10, 5
c = genfromtxt('foo.csv', delimiter=',')
d = c.reshape((x, y, z))
print(d)
