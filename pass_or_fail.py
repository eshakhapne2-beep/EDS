n = int(input())
marks = list(map(int,input().split()))
if any(mark < 40 for mark in marks):
	print("Fail")
else:
	aggrper= sum(marks)/n
	print("Aggregate Percentage: "+'%.2f'%aggrper)
	if aggrper>75:
		print("Grade: Distinction")
	elif 60<=aggrper<75:
		print("Grade: First Division")
	elif 50<=aggrper<60:
		print("Grade: Second Division")
	elif 40<=aggrper<50:
		print("Grade: Third Division")
	
