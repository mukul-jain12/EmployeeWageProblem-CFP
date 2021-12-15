"""Welcome To Employee Wage Problem"""
import random

EMP_RATE_PER_HOUR = 20
FULL_TIME = 8

emp_check = random.randrange(0, 2)

# checking attendance
if emp_check == 0:
    emp_hour = FULL_TIME
else:
    emp_hour = 0

# calculating employee wage
emp_wage = EMP_RATE_PER_HOUR * emp_hour
print(f"Monthly Wage of a Employee is :{emp_wage}")
