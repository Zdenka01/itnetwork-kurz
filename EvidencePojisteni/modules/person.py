class Person:
    def __init__(self, name, surname, age, phone):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone

    def __str__(self):
        return f"Person with name {self.name} {self.surname}, aged {self.age}, with phone number {self.phone}"