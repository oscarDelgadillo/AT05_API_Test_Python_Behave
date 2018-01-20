from Person import Person

class CommercialEmployee(Person):

    def __init__(self, name, pieces, department, num):
        super().__init__(name, pieces)
        self.department=department
        self.id="CE-"+str(num)
        self.salary=0
        self.discount=0

    def getId(self):
        return self.id

    def getSalary(self):
        return self.pieces*2.5

    def getDiscount(self):
        return self.getSalary()*12.5/100

    def getNetSalary(self):
        return self.getSalary()-self.getDiscount()

    def getEmployee(self):
        #return self.id
        #return self.id + " | " +  self.showPerson() + " | " + self.department + " | " +str(self.getSalary()) + " | " + str(self.getDiscount()) + " | " + str(self.getNetSalary())
        #return self.name
        return self.id + " | " + self.department + " | " + str(self.getSalary()) + " | " + str(self.getDiscount()) + " | " + str(self.getNetSalary())

