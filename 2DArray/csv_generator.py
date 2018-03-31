import numpy as np
a = np.random.randint(100, size=(1000, 1000))
np.savetxt("foo.csv", a, delimiter=",")
