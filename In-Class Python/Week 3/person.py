class Person:

    #__init__ is the class initializer - initializes instance variables of the object
    # use self to refer to the class attribute
    # first variable of any class method is self to refer to this instance of the class
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # __str__ returns a string representation of the object
    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def say_hello(self):
        print("Hello my name is", self.first_name)




