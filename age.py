from datetime import datetime
birth_year = int(input())
current_year = datetime.now().year
age = current_year - birth_year
print("AGE:" ,age)
