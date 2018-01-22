from person import Person


class Employee(Person):
    def __init__(self, first, last, employee_id, department):
        Person.__init__(self, first, last)
        self.employee_id = employee_id
        self.department = department
        self.total_sum_of_pieces_send = 0
        self.amount_of_effective_pieces = 0
        self.amount_of_defective_pieces = 0

    def get_id(self):
        return self.employee_id

    def get_department(self):
        return self.department

    def get_global_salary(self):
        if self.department == "Commercial":
            return self.total_sum_of_pieces_send * 2.5
        else:
            return (self.amount_of_defective_pieces * 1.3 +
                    self.amount_of_effective_pieces * 10)

    def get_discount(self):
        return self.get_global_salary() * 0.125

    def get_net_salary(self):
        return self.get_global_salary() - self.get_discount()

    def set_total_sum_of_pieces_send(self, total):
        self.total_sum_of_pieces_send = total

    def set_amount_of_effective_pieces(self, amount):
        self.amount_of_effective_pieces = amount

    def set_amount_of_defective_pieces(self, amount):
        self.amount_of_defective_pieces = amount
