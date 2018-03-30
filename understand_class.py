class Car:
    color = 'yellow'
    brand = 'BMW'


new_car = Car()   # every instance in this class
print(new_car.color)

class Customer:
    def __init__(self, name, age):
        self.name = name  # initial attributes
        self.age = age  # self means attributes change with the following instances


com_customer = Customer('Lucy', 15)  # instance

print(com_customer.name)