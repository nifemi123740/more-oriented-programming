class Employee:
    def __init__(self,name,emp_id):
        self.name = name
        self.emp_id = emp_id
        self.is_registered=False
    def register(self):
        if not self.is_registered:
            self.is_registered = True
            print(f"{self.name} has been successfully registered.")
        else:
            print(f"{self.name} is already registered.")
    def display(self):
        status = "Registered" if self.is_registered else "Not Registered"
        print(f"Name: {self.name}\nID: {self.emp_id}\nStatus: {status}")

employee1=Employee("Alice",'EMP00357')
employee1.display()
employee1.register()