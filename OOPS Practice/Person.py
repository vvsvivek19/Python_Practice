class Employee:
    def __init__(self):
        self.name = input("Please enter the name: ")
        try:
            self.phone = int(input("Please enter the phone number: "))
        except ValueError as mgs:
            print(f"Error: Phone number must have numbers and nothing else ({mgs})")
    def print_details(self):
        print(f"Person's name is {self.name} and his phone number is {self.phone}")

e = Employee()
e.print_details()
        