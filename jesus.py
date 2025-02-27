import numpy as np
a = np.array([int(input(f"número list1 {i+1} lista 1: ")) for i in range(5)])
b = np.array([int(input(f"numero list2 {i+1} lista 2: ")) for i in range(5)])
print(a * b)
