class Person:
    def __init__(self, name, last):
        self.name = name
        self.last_name = last
        # self.age = age
        # self.ci = ci

    def get_name(self):
        return self.name + " " + self.last_name

