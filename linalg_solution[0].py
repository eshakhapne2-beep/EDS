import numpy as np
A = np.array([[2,1],[1,3]])
b = np.array([70,110])
solution = np.linalg.solve(A,b)
print("price of 1 apple:", solution[0])
print("price of 1 milk:", solution[1])
