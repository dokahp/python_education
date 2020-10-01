class Patient:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return "{} {}. {}".format(self.name, self.last_name, self.age)

    def __repr__(self):
        return "Object of the class {}. name: {}, last_name: {}, age: {}".format(Patient.__name__, self.name,
                                                                                 self.last_name, self.age)
