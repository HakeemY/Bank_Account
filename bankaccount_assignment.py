class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance = 0): 
        self.int_rate = int_rate 
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            return self
        else:
            print("Insufficient funds")
            return self
        # withdraw(self, amount) 
        # - decreases the account balance by the given amount if there are sufficient funds; 
        # if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
        
    def display_account_info(self):
            print(f"Current account balance: ${self.balance}.")
            return self
    
    def yield_interest(self):
        if self.balance > 0:
           self.balance += self.balance * self.int_rate
        return self
        
account1 = BankAccount(0.01, 200)
account2 = BankAccount(0.02, 500)


account1.deposit(300).deposit(200).deposit(100).withdraw(100).yield_interest().display_account_info()
account2.deposit(500).deposit(400).withdraw(200).withdraw(100).withdraw(350).withdraw(100).yield_interest().display_account_info()
# # # increases the account balance by the current balance * the interest rate (as long as the balance is positive)

#---------------------------------------------------------------------
# Class Example
#---------------------------------------------------------------------
# class Human:
#     # name, age, race, color hair, dob, height, weight, language
#     def __init__(self, name, age, dob):
#         self.name = name
#         self.age = age
#         self.dob = dob
#         self.family_members = {}

#     def greet(self):
#         print(f"Hello, my name is {self.name} and my age is {self.age}!")
    
#     def birthday(self):
#         self.age += 1
#         if(self.age < 18):
#             print(f"Happy birthday {self.name}! You were born in {self.dob} and you are now {self.age}. Congrats, you still have your youth!")
#         if(self.age > 18):
#             print(f"Happy birthday {self.name}! You were born in {self.dob} and you are now {self.age}. Congrats, you are getting old!")
#         else:
#             print("Are you even born yet?!")

#     def add_family_member(self, name, age, dob):
#         obj1 = Human(name,age,dob)
#         self.family_members[name] = obj1


# hakeem = Human("Hakeem", 39, "03.08.1984")
# antoine = Human("Antoine", 35, "12.30.1988")

# print(antoine.age)

# hakeem.greet()
# antoine.greet()

# print(hakeem.age)
# hakeem.birthday()
# antoine.add_family_member("Bianca", 28, "07.31.94")
# print(antoine.family_members["Bianca"].dob)