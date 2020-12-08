class Person():
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def changeName(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def myInfo(self):
        print(self.firstname + " " + self.lastname)

class Customer(Person):
    def __init__(self, firstname, lastname, orderAmount, orderName):
        Person.__init__(self, firstname, lastname)
        self.order = Order(orderAmount, orderName)
        self.receivedOrder = False
    
    def receivedOrder(self):
        self.receivedOrder = True
    
    def getOrder(self):
        return self.order.item
    
    def getAmount(self):
        return self.order.amount

    def myInfo(self):
        print(self.firstname + " " + self.lastname)
        print("Item: " + self.getOrder())
        print("Order Total: " + str(self.getAmount()))

class Order():
    def __init__(self, amount, item):
        self.amount = amount
        self.item = item

class Driver(Person):
    def __init__(self, firstname, lastname, customer):
        Person.__init__(self, firstname, lastname)
        self.customerOrder = customer.getOrder()

menu = ["1: Apple Pie", "2: Banana Pie", "3: Mango Pie"]
prices = [10.75, 15.45, 12.42]

check = input("Would you like to put in a delivery order? y/n")
while check == "y":
    firstname = input("What is the customer's first name?")
    lastname = input("What is the customer's last name? ")
    order = int(input("What is the order number (1-3)? "))
    currentCustomer = Customer(firstname, lastname, prices[order-1], menu[order-1])
    print("Here is the current customer info: ")
    currentCustomer.myInfo()

    check = input("Would you like to put in another delivery order? y/n")





