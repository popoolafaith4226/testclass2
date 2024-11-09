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
        """
        Initializes a Person object with the given attributes.

        Args:
            name (str): The person's name.
            gender (str): The person's gender (optional).
            age (int): The person's age (optional).
        """

        self.name = name
        self.gender = gender  # Default value can be provided here, e.g., "unknown"
        self.age = age  # Default value can be provided here, e.g., 0

    def myfunc(self):
        """
        Prints a greeting message with the person's name.
        """

        print(f"Hello, my name is {self.name}.")

# Create an instance of the Person class with appropriate arguments
p1 = Person("Faith", "Female", 11)  # Modify arguments as needed

# Call the myfunc() method on the created object
p1.myfunc()