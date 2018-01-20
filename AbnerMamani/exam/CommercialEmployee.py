from Person import Person

class Employee(Person):

    def __init__(self, name, lastName, age, ci, empployeeId, department):
        super().__init__(name, lastName, age, ci)
        self.employeeId=empployeeId
        self.department=department

    def getEmployee(self):
        return self.fullName() + " " + self.employeeId + " " +self.department

per = Person("Juan", "Carpas", "28", "5247889")
emp = Employee("Pablo", "Peredo", "50", "1237889", "123", "sales")

print(per.fullName())
print(emp.getEmployee())