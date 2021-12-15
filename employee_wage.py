"""Welcome To Employee Wage Problem"""
import random

EMP_RATE_PER_HOUR = 20
FULL_TIME = 8
PART_TIME = 4

emp_check = random.randrange(0, 3)

# checking attendance
if emp_check == 0:
    emp_hour = FULL_TIME
elif emp_check == 1:
    emp_hour = PART_TIME
else:
    emp_hour = 0

# calculating employee wage
emp_wage = EMP_RATE_PER_HOUR * emp_hour
print(f"Monthly Wage of a Employee is :{emp_wage}")
