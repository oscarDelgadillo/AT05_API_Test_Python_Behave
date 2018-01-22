# Module: staff
from AT05_API_Test_Python_Behave.FrancoAldunate.python_exam.utilities.calculations import *
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Person():
    # Class constructor
    def __init__(self, id, name, department):
        self.employee_id = id
        self.employee_name = name
        self.employee_department = department
        self.global_salary = 0
        self.total_discount = 0
        self.net_salary = 0

    def calculate_global_salary(self):
        pass

    def calculate_discount(self):
        self.total_discount = calculate_discount(self.global_salary)
        return self.total_discount

    def calculate_net_salary(self):
        self.net_salary = calculate_net_salary(self.global_salary, self.total_discount)
        return self.net_salary

    def get_employee_id(self):
        return self.employee_id

    def get_employee_name(self):
        return self.employee_name

    def get_employee_department(self):
        return self.employee_department

    def get_global_salary(self):
        return self.global_salary

    def get_total_discount(self):
        return self.total_discount

    def get_net_salary(self):
        return self.net_salary

    def print_data(self):
        print("Employee ID | Name | Department | Global Salary | Total Discount | Net Salary")
        print(
            f"{self.employee_id} | {self.employee_name} | {self.employee_department} | {self.global_salary} | {self.total_discount} | {self.net_salary}")
