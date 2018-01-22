# Module: employees
from AT05_API_Test_Python_Behave.FrancoAldunate.python_exam.company.human_resources import Person
from AT05_API_Test_Python_Behave.FrancoAldunate.python_exam.utilities.calculations import *
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class CommercialEmployee(Person):
    # Class constructor
    def __init__(self, id, name, department, amount_of_pieces_sell):
        super().__init__(id, name, department)
        self.amount_of_pieces_sell = amount_of_pieces_sell

    def calculate_global_salary(self):
        self.global_salary = self.amount_of_pieces_sell * 25
        return self.global_salary


class ProductionEmployee(Person):
    # Class constructor
    def __init__(self, id, name, department, amount_of_pieces_produced, amount_of_defective_pieces):
        super().__init__(id, name, department)
        self.amount_of_pieces_produced = amount_of_pieces_produced
        self.amount_of_defective_pieces = amount_of_defective_pieces

    def calculate_global_salary(self):
        self.global_salary = (self.amount_of_pieces_produced * 10) - (self.amount_of_defective_pieces * 1.3)
        return self.global_salary
