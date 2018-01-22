# Module: main
from AT05_API_Test_Python_Behave.FrancoAldunate.python_exam.company.employees import *
from AT05_API_Test_Python_Behave.FrancoAldunate.python_exam.company.human_resources import *
from AT05_API_Test_Python_Behave.FrancoAldunate.python_exam.utilities.calculations import *
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

employees = []


class PickupItems():
    # Class constructor
    # def __init__(self):

    # self.employees = []

    # Function: pick up item
    def register_employee(self):
        logger.info("Starting execution...")
        employees_amount = int(input("Insert amount of employees between 3 and 15: "))
        if 2 < employees_amount < 16:
            for i in range(employees_amount):
                employee_name = input("Employee name?: ")
                employee_department = input("Employee department?: ")
                if employee_department.lower() == "commercial":
                    amount_of_pieces_sell = int(input("Employee amount of pieces sell?: "))
                    logger.info("Creating employee instance")
                    commercialEmployee = CommercialEmployee(generate_id("CE_0", i), employee_name, employee_department,
                                                            amount_of_pieces_sell)
                    commercialEmployee.calculate_global_salary()
                    commercialEmployee.calculate_discount()
                    commercialEmployee.calculate_net_salary()
                    logger.debug('Records: %s', commercialEmployee.print_data())
                    employees.append(commercialEmployee)
                elif employee_department.lower() == "production":
                    logger.info("Creating employee instance")
                    amount_of_pieces_produced = int(input("Employee amount of pieces produced?: "))
                    amount_of_defective_pieces = int(input("Employee amount of defective pieces?: "))
                    productionEmployee = ProductionEmployee(generate_id("PE_0", i), employee_name, employee_department,
                                                            amount_of_pieces_produced, amount_of_defective_pieces)
                    productionEmployee.calculate_global_salary()
                    productionEmployee.calculate_discount()
                    productionEmployee.calculate_net_salary()
                    logger.debug('Records: %s', productionEmployee.print_data())
                    employees.append(productionEmployee)
        else:
            print("Invalid input")
            logger.info("Invalid input")

pickupItems = PickupItems()
pickupItems.register_employee()
