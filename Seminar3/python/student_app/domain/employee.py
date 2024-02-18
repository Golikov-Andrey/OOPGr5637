from domain.person import Person

class Employee(Person):
    def __init__(self, firstName, age, special):
        super().__init__(firstName, age)
        self.special = special