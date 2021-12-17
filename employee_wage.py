"""Welcome To Employee Wage Problem"""
import random


class EmployeeWage:
    # constants
    EMP_RATE_PER_HOUR = 20
    FULL_TIME = 8
    PART_TIME = 4
    WORKING_HOURS = 100

    def employee_monthly_wage(self):
        """
            desc: calculating monthly wage of employee
            return: monthly wage
        """
        working_days = 0
        total_emp_hour = 0

        while working_days < 20 and total_emp_hour <= self.WORKING_HOURS:
            working_days += 1
            emp_check = random.randrange(0, 3)

            # checking full-timme, part-time or absent
            emp_hour = self.calculate_emp_hours(emp_check)

            total_emp_hour += emp_hour

            if total_emp_hour > 100:
                total_emp_hour -= emp_hour
                break

        # calculating monthly wage of employee
        emp_wage = self.calculate_emp_wage(self.EMP_RATE_PER_HOUR, total_emp_hour)
        print(f"Monthly Wage of a Employee is : {emp_wage}")

    def calculate_emp_hours(self, emp_check):
        """
            desc: calculate daily hours of employee
            param: emp_check:
            return: employee hour(int value)
        """
        if emp_check == 0:
            return self.FULL_TIME
        elif emp_check == 1:
            return self.PART_TIME
        else:
            return 0

    def calculate_emp_wage(self, rate_per_hour, total_hour):
        """
            desc: calculating total employee wage
            param1: rate_per_hour:
            param2: total_hour:
            return: employee wage
        """
        employee_wage = rate_per_hour * total_hour
        return employee_wage


if __name__ == '__main__':
    """
        Calling the calculate_monthly_wage function in EmployeeWage class
        to calculate monthly wage of employee.
    """
    emp_monthly_wage = EmployeeWage()

    emp_monthly_wage.employee_monthly_wage()
