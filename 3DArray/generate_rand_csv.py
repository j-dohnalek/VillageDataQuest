import numpy as np

x, y, z = 10, 10, 5
a = np.random.randint(5, size=(x, y, z))
b = a.reshape(1, x*y*z)
np.savetxt('foo.csv', b, delimiter=',')
