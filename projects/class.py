#classes allow us to logically group our data(atributes) and functions(methods) in a way thats easy to reuse and build apon of

class Employee: #classes are blueprints for creating instances each unique Employee you create will be an instance of that class
    def __init__(self, first , last , pay) -> None: # this method is considered the constructor, creating methods within a class they receive instances as the frist argument such as self
        self.first = first
        self.last = last
        self.pay  = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee("Corey",'Schafer',50000) # each will be one instance of the class they are unique
emp_2 = Employee('Test','User',60000)

Employee.fullname(emp_2)
print(emp_2.fullname())



