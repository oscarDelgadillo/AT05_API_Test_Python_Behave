class Person:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def get_name(self):
        return self.firstname + " " + self.lastname
