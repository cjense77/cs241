import numpy as np

def f(n):
    return 2**((2**n - 1)/(2**n))

x = np.sqrt(2)

for i in range(1, 20):
    print(np.abs(x - f(i)))
    x = np.sqrt(2*x)