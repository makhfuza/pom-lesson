class Employee:

    vacation_days = 20


class Tester(Employee):
    
    # class constructor, template, initializer
    def __init__(self, name, tittle) -> None:
        self.name = name
        self.title = tittle

    def get_employee_details(self):
       print("Name : ", self.name,  ", Title: ", self.title)
      

Mike = Tester('Mike', 'CEO')
Jennifer = Tester('Jennifer', 'Manager')

