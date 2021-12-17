"""Welcome To Employee Wage Problem"""
import random


class EmployeeWage:
    # constants
    FULL_TIME = 8
    PART_TIME = 4

    def employee_monthly_wage(self, company, emp_rate_per_hour, working_day, working_hours):
        """
            desc: calculating monthly wage of employee
            return: monthly wage
        """
        working_days = 0
        total_emp_hour = 0

        while working_days < working_day and total_emp_hour <= working_hours:
            working_days += 1
            emp_check = random.randrange(0, 3)

            # checking full-timme, part-time or absent
            emp_hour = self.calculate_emp_hours(emp_check)

            total_emp_hour += emp_hour

            if total_emp_hour > 100:
                total_emp_hour -= emp_hour
                break

        # calculating monthly wage of employee0
        emp_wage = self.calculate_emp_wage(emp_rate_per_hour, total_emp_hour)
        print(f"Monthly Wage of a Employee in a {company} is : {emp_wage}")

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
        to calculate monthly wage of employee for multiple companies.
    """
    emp_monthly_wage = EmployeeWage()

    emp_monthly_wage.employee_monthly_wage("Tata", 20, 20, 100)
    emp_monthly_wage.employee_monthly_wage("LTI", 30, 24, 150)
    emp_monthly_wage.employee_monthly_wage("Accenture", 25, 22, 130)
    emp_monthly_wage.employee_monthly_wage("JIO", 40, 28, 160)
