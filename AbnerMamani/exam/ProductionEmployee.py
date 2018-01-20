from Person import Person


class ProductionEmployee(Person):
    def __init__(self, name, pieces, piecesDef, department, num):
        super().__init__(name, pieces)
        self.pieceDef=piecesDef
        self.department = department
        self.id = "PE-" + str(num)
        self.salary = 0
        self.discount = 0

    def getId(self):
        return self.id

    def getSalary(self):
        return (self.pieces * 10) + (self.pieceDef*1.3)

    def getDiscount(self):
        return self.getSalary() * 12.5/100

    def getNetSalary(self):
        return self.getSalary() - self.getDiscount()


    def getEmployee(self):
        #return self.id + " | "   + self.department + " | " + str(self.getSalary())
        return self.id + " | "  + self.department + " | " + str(self.getSalary()) + " | " + str(self.getDiscount()) + " | " + str(self.getNetSalary())


