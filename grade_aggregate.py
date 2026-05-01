def cal(marks,total_course):
    total_marks = sum(marks)
    aggregate_percentage = (total_marks / (total_course * 100)) * 100
    if any(mark <= 40 for mark in marks):
        return "fail"
    if (aggregate_percentage > 75):
        grade = "distinction"
    elif (aggregate_percentage >= 60):
        grade = "first division"
    elif (aggregate_percentage >=50):
        grade = "second division"
    elif(aggregate_percentage >=40):
        grade = "third division"

        return (aggregate_percentage,grade)
    total_course = int(input())
    marks = list(map(int(input().split())))
    result = cal(total_course,marks)
    if result == "fail":
        print("fail")
    else:
        result = aggregate_percentage,grade
        print(f"aggregate_percentage:{aggregate_percentage:.2f}")
        print(f"grade:{grade}")
    
