"""Welcome To Employee Wage Problem"""
import random

EMP_RATE_PER_HOUR = 20
FULL_TIME = 8
PART_TIME = 4

WORKING_DAYS = 20
total_emp_hour = 0

for day in range(1, WORKING_DAYS+1):
    emp_check = random.randrange(0, 3)

    # checking attendance
    if emp_check == 0:
        emp_hour = FULL_TIME
    elif emp_check == 1:
        emp_hour = PART_TIME
    else:
        emp_hour = 0

    total_emp_hour += emp_hour

# calculating monthly wage of employee
emp_wage = EMP_RATE_PER_HOUR * total_emp_hour
print(f"Monthly Wage of a Employee is :{emp_wage}")
