from datetime import datetime
def cal_age(birth_date):
    birth_year = int(input(split("-")[-1]))
    current_year = datetime.now().year
    return(current_year - birth_year)
def convert_salary(salary_INR):
    conversion_rate = 0.012
    return(salary_INR * conversion_rate)
birth_year = int(input())

    
    
