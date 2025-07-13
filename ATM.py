class ATM:
    # constructor() it is a special function
    def __init__(self):
        print("self ka address ",id(self))
        self.pin = " "
        self.balance = 0

        # self.menu()
    def menu(self):
        user_input = input("""
        Hi how can I help you? 
        1. Press  1 to create pin
        2. Press 2 to change pin
        3. Press 3 to check balence
        4. Press 4 to withdraw
        5. Press 5 to deposit money
        6. Anything else to exit
        """)
        # create pin for press 1
        if user_input == "1": 
            self.create_pin()
        # change pin for press 2
        elif user_input == "2":
            self.change_pin()
        # check balance for press 
        elif user_input == "3":
            self.check_balance()
        # withdraw money for press 4
        elif user_input == "4":
            self.withdraw()
        elif user_input == "5":
            self.deposit()
        # anything else to exit for press 5
        else:
            print("Invalid input")
            exit()
    def create_pin(self):
        user_pin = input("Enter you pin")
        self.pin = user_pin
        user_balance = int(input("Enter balance "))
        self.balance = user_balance
        print("pin created successfully")
        self.menu()
       
    def change_pin(self):
        old_pin = input("enter old pin: ")
        if old_pin == self.pin:
            # let him change the pin
            new_pin = input("enter new pin")
            self.pin = new_pin
            print("Pin change successfull")
            self.menu()
        else:
            print("Mai nhi krne de sakta re baba")
            self.menu()
    def check_balance(self):
        user_pin = input("Enter you pin: ")
        if user_pin == self.pin:
            print("You balance is ", self.balance)
            self.menu()
        else:
            print("Wrong password: ")
            self.menu()
           
    def withdraw(self):
        user_pin = input("enter the pin: ")
        if user_pin == self.pin:
            # allow to withdrawl
            amount = int(input("Enter the amount: "))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print("Withdraw successfull and remaining balance si ", self.balance)
                self.menu()
            else:
                print("bhag garib")
                self.menu()
            
        else:
                print("Wrong password")
                self.menu()
    def deposit(self):
        dep_amout = int(input("Enter the amount: "))
        self.balance = dep_amout + self.balance
        self.menu()
        
obj = ATM()
print("the Address of obj is equal to the self: ",id(obj))
# class ka chizo ak shirf class ka object access kr sakta h
# ek class dushro class ka funciton ko access nhi kr skta 

# to agar ek class dushre class ka funciton ko call krna possible ho skta h to by using the self(object)
