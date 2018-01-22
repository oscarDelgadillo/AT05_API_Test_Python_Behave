import classPerson


class Employee(classPerson.Person):
    def __init__(self, first, last, age, ci, id, department):
        super().__init__(first, last, age, ci)
        self.id = id
        self.department = department

    def getEmployee(self):
        return self.getPerson() + " " + self.id + " " + self.department
