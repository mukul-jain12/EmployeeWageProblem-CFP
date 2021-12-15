"""Welcome To Employee Wage Problem"""
import random

EMP_RATE_PER_HOUR = 20
FULL_TIME = 8
PART_TIME = 4
WORKING_HOURS = 100

working_days = 0
total_emp_hour = 0

while working_days < 20 and total_emp_hour <= WORKING_HOURS:
    working_days += 1
    emp_check = random.randrange(0, 3)

    # checking full-timme, part-time or absent
    if emp_check == 0:
        emp_hour = FULL_TIME
    elif emp_check == 1:
        emp_hour = PART_TIME
    else:
        emp_hour = 0

    total_emp_hour += emp_hour

    if total_emp_hour > 100:
        total_emp_hour -= emp_hour
        break

# calculating monthly wage of employee
emp_wage = EMP_RATE_PER_HOUR * total_emp_hour
print(f"Monthly Wage of a Employee is :{emp_wage}")
