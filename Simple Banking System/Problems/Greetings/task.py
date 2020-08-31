class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, I am {name}!".format(name=self.name))


input_name = input()
greet = Person(input_name)
greet.greet()
