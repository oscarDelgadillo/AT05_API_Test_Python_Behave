class Person:

    def __init__(self, name, _lastName, _age, _ci):
        self.name = name
        self.lastName = _lastName
        self.age=_age
        self.ci=_ci

    def fullName(self):
        return self.name + " " + self.lastName + " " + self.age + " " + self.ci


