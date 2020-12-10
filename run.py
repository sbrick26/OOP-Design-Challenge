class Person():
    def __init__(self, firstname, lastname):
        self.__firstname = firstname
        self.__lastname = lastname
    
    def changeName(self, firstname, lastname):
        self.__firstname = firstname
        self.__lastname = lastname

    def returnName(self):
        return self.__firstname + " " + self.__lastname

    def myInfo(self):
        print(self.__firstname + " " + self.__lastname)

class Customer(Person):
    def __init__(self, firstname, lastname, orderAmount, orderName):
        Person.__init__(self, firstname, lastname)
        self.order = Order(orderAmount, orderName)
        self.receivedOrder = False
    
    def orderDone(self):
        self.receivedOrder = True
    
    def getOrder(self):
        return self.order.item
    
    def getAmount(self):
        return self.order.amount

    def hasReceived(self):
        return self.receivedOrder
    
    def myInfo(self):
        print(self.returnName())
        print("Item: " + self.getOrder())
        print("Order Total: " + str(self.getAmount()))

class Order():
    def __init__(self, amount, item):
        self.amount = amount
        self.item = item
    
    def orderInfo(self):
        return self.item + ": " + self.amount
    
    def changeItem(self, index):
        self.amount = prices[index - 1]
        self.item = menu[index - 1]        

class Driver(Person):
    def __init__(self, firstname, lastname, customer):
        Person.__init__(self, firstname, lastname)
        self.customer = customer
    
    def delievered(self):
        self.customer.orderDone()

    def check(self):
        print("Delivery Successful: " + str(self.customer.hasReceived()))
    
    def myInfo(self):
        print("Driver Info")
        print(self.returnName())
        print("Customer Info")
        self.customer.myInfo()


menu = ["1: Apple Pie", "2: Banana Pie", "3: Mango Pie"]
prices = [10.75, 15.45, 12.42]

check = input("Would you like to put in a delivery order? (y/n): ")
while check == "y":
    firstname = input("What is the customer's first name? ")
    lastname = input("What is the customer's last name? ")
    print()
    for item in menu:
        print(item)
    
    print()
    order = int(input("What is the order number (1-3)? "))
    
    currentCustomer = Customer(firstname, lastname, prices[order-1], menu[order-1])
    print()
    print("Here is the current customer info: ")
    currentCustomer.myInfo()
    print()
    checkName = input("Is this the correct info? (y/n): ")
    if checkName == "n":
        firstname = input("What is the customer's first name? ")
        lastname = input("What is the customer's last name? ")
        currentCustomer.changeName(firstname, lastname)
        print()
        print("Here is the current customer info: ")
        currentCustomer.myInfo()


    print("Assigning Driver...")
    currentDriver = Driver("Swayam", "Barik", currentCustomer)
    print()
    currentDriver.myInfo()
    
    driverCheck = "n"
    print()
    while driverCheck != "y":
        driverCheck = input("Has the item been delievered? (y/n): ")
    print()
    currentDriver.delievered()
    currentDriver.check()

    print()
    check = input("Would you like to put in another delivery order? (y/n): ")





