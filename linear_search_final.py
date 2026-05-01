A = list(map(int,input().split()))
key = int(input())
if key in A:
	print(A.index(key))
else:
	print("Not found")
