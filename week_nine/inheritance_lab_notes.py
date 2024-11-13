# Inheritance = a class declared as a subclass of another class.
# > The subclass(child) receives all the code of the super(parent) class.
# > Two goals of inheritance are promoting code reusability &
# > preventing repeated code

# >>Example 1<<
# class Parent():
#     def __init__(self):
#         pass
# class Child(Parent):
#     def __init__(self):
#         super().__init__() #inherits from parent

# # A subclass(child) can be the parent of another class

# # >>Example 2<<
# class Grandparent():
#     def __init__(self):
#         self.x = 3
# class Parent(Grandparent): #inherits from Grandparent
#     def __init__(self):
#         super().__init__()
# class Child(Parent): #inherits from Parent
#     def __init__(self):
#         super().__init__()

# c = Child()
# # print(c.x) # prints 3 from Grandparent

# # Inheritance if normally used for 'x' 'is a type of' 'y' relationships
# # >(in online lab diagram) an arrow pointing from one object to another
# # means 'is a type of,' for example Bluejay 'is a type of' Bird

# #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # GAME Example: (Check notebook/phone/lab for diagram)
# # An arrow from Hobgoblin -> Goblin means Hobgoblin 'is a type of'
# # Goblin. Arrow also = 'inherits from' as in Hobgoblin will inherit
# # all the code from Goblin. This is useful because the game could
# # have goblins that behave 'goblin-y' but maybe they are stronger
# # and look tougher and they drop better loot. 
# # So we reuse as much of the code as possible using inheritance
# # (OF INTEREST!)
# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # >Overriding 
# # Can redefine the method using the same name and parameter list. 
# # The subclass version will be called. The subclass can choose to
# # call the superclass' version. Python starts at the type of our 
# # object being called and checking if that method exists.
# # Python will check the super classes all the way up the line
# # until it reaches the Object class. If method is not found,
# # an error is raised.
  
# # ! Learn to use the __repr__ function!
# # When using the __repr__ function, we are overriding the object
# # class'default __repr__ method.

# # >Multiple Inheritance
# class A:
#     def a(self):
#         print('a')
# class B():
#     def b(self):
#         print('b')
# class C(A,B): # C inherits both A and B
#     def c(self):
#         self.a()
#         self.b()
# c = C()
# c.c()
# # ^Output =
# # a
# # b

# >Practice
# Bank class that holds bank accounts and can accrue monthly
# interest on all accounts

class Bank:
    def __init__(self):
        self.accounts = {}

    def monthly_interest(self):
        for account in self.accounts.values(): account.accrue()
    
    def add_account(self, accnt):
        self.accounts[accnt.owner] = accnt
    
    def withdraw(self, name, val):
        self.accounts[name].money -= val
        if self.accounts[name].money < 0:
            self.accounts[name].money -= 5

    def deposit(self, name, val):
        self.accounts[name].money += val

    def __repr__(self):
        return 'Bank:\n'+'\n'.join(f'\t{x}' for x in self.accounts.values())
    

# Account class, not type of bank so wont inherit from bank.
# can deposit, withdraw, and accrue. Meant to be inherited from
class Account:
    def __init__(self, owner, money):
        self.owner, self.money = owner, money
    
    def deposit(self, amt):
        if amt > 0: # can't deposit negative money.
            self.money += amt
    
    def withdraw(self, amt): 
        self.money -= amt
        if self.money < 0:
            self.money -= 5

    def accrue(self):
        raise NotImplementedError('child class must implement accrue')
    
    def __repr__(self):
        owner_cap = self.owner.capitalize()
        return f'Owner: {owner_cap}, Balance: ${self.money:.2f}'
    
# Checking
class Checking(Account):
    def accrue(self):
        # $50 fine for owing money at the end of the month
        if self.money < 0: 
            self.money -= 50
        # otherwise gain 6% interest
        else: 
            self.money *= 1.06

# Savings 
# savings is a type of account so we choose to inherit from account.
# withdrawing from account is penalized with a flat fee, but 
# owner gets a higher return per month.
class Savings(Account):
    #overriding withdraw
    def withdraw(self, amt):
        self.money -= 20 #$20 flat fee for withdrawing from savings
        return super().withdraw(amt)
    def accrue(self):
        if self.money < 0: 
            self.money -= 100
        else: 
            self.money *= 1.10

# Lab----------------------------

class FatCat(Account):
    def accrue(self):
        if self.money < 1_000_000: self.money -= 50_000
        else: self.money *= 1.30

# alice = Checking('Alice' , 20_000)
# bob = Savings('Bob' , 4_000)
# scrooge = FatCat('Scrooge' , 1_000_000_000)

b = Bank()
# for accnt in alice, bob, scrooge: 
#   b.add_account(accnt)

# bob.deposit(100)
# alice.withdraw(500)

# b.monthly_interest()
# print(b)

num_accnts = int(input('Please input number of accounts: '))

for num in range(num_accnts):
    accnt_info = input('Please enter the account type, owner, and starting amount: ').split()
    temp = 0
    if accnt_info[0].lower().strip() == 'checking':
        temp = Checking(accnt_info[1].lower().strip(), float(accnt_info[2]))
        b.add_account(temp)
    
    if accnt_info[0].lower().strip() == 'savings':
        temp = Savings(accnt_info[1].lower().strip(), float(accnt_info[2]))
        b.add_account(temp)

    if accnt_info[0].lower().strip() == 'fatcat':
        temp = FatCat(accnt_info[1].lower().strip(), float(accnt_info[2]))
        b.add_account(temp)

print(b) #checkin to make sure accounts are added

num_cmmnds = int(input('\nPlease state the number of commands: '))

for num in range(num_cmmnds):
    cmmnd = input("Please enter 'deposit' or 'withdraw' along with the account name and amount. \nOr enter 'monthly_interest.': ").split()
    
    if cmmnd[0].lower().strip() == 'deposit':
        b.accounts[cmmnd[1]].deposit(float(cmmnd[2]))

    if cmmnd[0].lower().strip() == 'withdraw':
        b.accounts[cmmnd[1]].withdraw(float(cmmnd[2]))

    if cmmnd[0].lower().strip() == 'monthly_interest':
        b.monthly_interest()

print(b)