import classPerson


class Employee(classPerson.Person):
    def __init__(self, employee_id, first, last, department, pieces_sell, pieces_prod, pieces_def):
        super().__init__(first, last)
        self.employee_id = employee_id
        self.department = department
        self.pieces_sell = pieces_sell
        self.pieces_prod = pieces_prod
        self.pieces_def = pieces_def

    def get_employee(self):
        salary = global_salary(self.department, self.pieces_sell, self.pieces_prod, self.pieces_def)
        discount = salary * 0.125
        net_salary = salary - discount
        return self.employee_id + "\t | " + self.get_name() + "\t | " + get_department(self.department) + \
               "\t | " + str(round(salary, 2)) + "\t | " + str(round(discount, 2)) + "\t | " + str(round(net_salary, 2))


def get_department(department):
    if department == 'c':
        return "Commercial"
    elif department == 'p':
        return "Production"


def global_salary(department, sell, prod, defec):
    if department == 'c':
        return sell * 2.5
    elif department == 'p':
        return (prod * 10) + (defec * 1.3)
