num = []
while True:
	print("1. Add")
	print("2. Remove")
	print("3. Display")
	print("4. Quit")
	choice = input("Enter choice: ")
	if choice == '1':
		n = int(input("Integer: "))
		if n >= 0:
			num.append(int(n))
			print("List after adding:",num)
		else:
			print("Invalid input")
	elif choice == '2':
		if len(num)==0:
			print("List is empty")
		else:
			n = int(input("Integer: "))
			if n in num:
				num.remove(n)
				print("List after removing:", num)
			else:
				print("Element not found")
	elif choice == '3':
		if len(num) == 0:
			print("List is empty")
		else:
			print(num)
	elif choice == "4":
		break

	else:
		print("Invalid choice")


