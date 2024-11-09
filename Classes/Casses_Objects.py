#Every Instance in python is an object
# class is like a blueprint for similar object

# class Person:
#     def __init__(self, name,gender,age):
#         self.name = "Faith"
#         self.gender = "Male"
#         self.age = 11
#
#     def myfunc(self):
#             print("Hello my name is " + self.name)
#
#     p1 = Person("name", age)
#     p1.myfunc()

class Person:
    def __init__(self, name, gender, age):


        self.name = name
        self.gender = gender
        self.age = age

    def myfunc(self):
        """
        Prints a greeting message with the person's name.
        """

        print(f"Hello, my name is {self.name}.")


p1 = Person("Faith", "Female", 11)


p1.myfunc()