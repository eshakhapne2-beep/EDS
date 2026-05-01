import numpy as np

# write your code here...
r,c = map(int,input().split())
elements = []
for i in range(r):
	elements.extend(map(int,input().split()))
arr = np.array(elements)
arr = arr.reshape(r,c)
print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)
