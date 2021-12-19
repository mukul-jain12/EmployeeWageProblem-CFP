"""Welcome To Employee Wage Problem"""
import random


class CompanyEmpWage:
    total_emp_wage = 0

    def __init__(self, company, emp_rate_per_hour, working_day, working_hours):
        self.company = company
        self.emp_rate_per_hour = emp_rate_per_hour
        self.working_day = working_day
        self.working_hours = working_hours

    def total_emp_wage(self, total_emp_wage):
        self.total_emp_wage = total_emp_wage

    def __str__(self):
        return self.company, self.total_emp_wage


class EmployeeWage:
    # constants
    FULL_TIME = 8
    PART_TIME = 4
    __numOfCompanies = 0
    __company_employee_wage_list = []

    def __init__(self):
        self.company = 0
        self.emp_rate_per_hour = 0
        self.working_day = 0
        self.working_hours = 0

    def add_company(self, company, emp_rate_per_hour, working_day, working_hours):
        """
            desc: append the company details in the list
            :param company:
            :param emp_rate_per_hour:
            :param working_day:
            :param working_hours:
        """
        self.company = company
        self.emp_rate_per_hour = emp_rate_per_hour
        self.working_day = working_day
        self.working_hours = working_hours
        self.__company_employee_wage_list.append(CompanyEmpWage(self.company, self.emp_rate_per_hour, self.working_day, self.working_hours))
        self.__numOfCompanies += 1

    def compute_wage(self):
        """
            desc: populating total emp wage after computing
        """
        for i in range(self.__numOfCompanies):
            self.__company_employee_wage_list[i].total_emp_wage(self.__employee_monthly_wage(self.__company_employee_wage_list[i]))

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

    def __employee_monthly_wage(self, __company_employee_wage_list):
        """
            desc: calculating monthly wage of employee
            return: monthly wage
        """
        working_days = 0
        total_emp_hour = 0
        emp_daily_wage = []

        while working_days < __company_employee_wage_list.working_day and total_emp_hour <= __company_employee_wage_list.working_hours:
            working_days += 1
            emp_check = random.randrange(0, 3)

            # checking full-timme, part-time or absent
            emp_hour = self.calculate_emp_hours(emp_check)

            total_emp_hour += emp_hour

            if total_emp_hour > 100:
                total_emp_hour -= emp_hour
                break
            emp_daily_wage.append(__company_employee_wage_list.emp_rate_per_hour * emp_hour)

        # calculating monthly wage of employee0
        emp_wage = self.calculate_emp_wage(__company_employee_wage_list.emp_rate_per_hour, total_emp_hour)
        print(f"Monthly Wage And Daily Wage List of a Employee in a {__company_employee_wage_list.company} is : {emp_wage} and {emp_daily_wage}")
        return self.company, emp_wage, emp_daily_wage


if __name__ == '__main__':
    """
        Calling the calculate_monthly_wage function in EmployeeWage class
        to calculate monthly wage of employee for multiple companies.
    """
    emp_monthly_wage = EmployeeWage()

    emp_monthly_wage.add_company("Tata", 20, 20, 100)
    emp_monthly_wage.add_company("LTI", 30, 24, 150)
    emp_monthly_wage.add_company("Accenture", 25, 22, 130)
    emp_monthly_wage.add_company("JIO", 40, 28, 160)

    emp_monthly_wage.compute_wage()

