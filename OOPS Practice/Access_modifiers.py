class Employee:
    def __init__(self, name, salary):
        # public member
        self.name = name
        # private member
        # not accessible outside of a class
        self.__salary = salary

    def show(self):
        print("Name is ", self.name, "and salary is", self.__salary)
    def __private_function(self):
        print("This is private function")
    def call_private(self):
        print("Calling Private Function")
        self.__private_function()

emp = Employee("Jessa", 40000)
emp.show()

#accessing a private function with the help of instance method
emp.call_private()

#calling a private function directly with object
emp.__private_function()

# access salary from outside of a class
print(emp.__salary)
