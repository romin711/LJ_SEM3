# class AgeValidationError(Exception):
#     pass

# def validate_age(age):
#     if age < 18:
#         raise AgeValidationError("Age must be 18 or above")
#     else:
#         print('valid age')
# try:
#     age = int(input('Enter age: '))
#     validate_age(age)
# except Exception as e:
#     print(e)
#     print(type(e))
#     print(e.__class__.__name__)


# wap for library book record with OOP in this programme it will ask user for add book and display books.
# class Library:
#     def __init__(self):
#         self.title = ''
#         self.author = ''
#         self.publication = ''
#     def read(self):
#         self.title = input('enter title: ')
#         self.author = input('enter author: ')
#         self.publication = input('enter publication: ')
#     def display(self):
#         print('title: ', self.title, 'author: ', self.author, 'publication: ', self.publication)
# my_book = []
# ch = 'y'
# while (ch == 'y'):
#     print('enter 1 for add books\nenter 2 for display books')
#     choice = int(input('enter your choice: '))
#     if choice == 1:
#         book = Library()
#         book.read()
#         my_book.append(book)
#     elif choice == 2:
#         for i in my_book: 
#             i.display()
#     else:
#         print('enter valid choice: ')
#     ch = input('do you want to counitnue...? : ')


# 541
# class BankAccount:
#     def __init__(self , account_number , name, balance):
#         self.account_number = account_number
#         self.name = name
#         self.balance = balance
    
#     def deposite(self , amount):
#         if amount > 0:
#             self.balance += amount
#             print('deposited: ',amount , 'new valance: ', self.balance)
#         else:
#              print('insufficient balance')
        
#         def withdrawl(self , amount):
#             if amount>0:
#                 if self.balance >= amount:
#                     self.balance -= amount
#                     print('withdra: ', amount , 'new balance: ',self.balance)
#                 else:
#                     print('insufficient balance')
#             else:
#                 print('withdraw amount must be +ve')

#         def display(self):
#             print('account number: ',self.account_number)
#             print('name: ',self.name)
#             print('balance: ',self.balance)

# acc_num = input('enter acc number: ') 
# name = input('entyer your name')
# balance = input('enter initial balance')
# account1 = BankAccount(acc_num , name, balance)
# account1.display()

# deposite_amm = input('enter amount to deposite')
# account1.deposite(deposite_amm)

# withdraw_amm = input('enter amount to withdraw')
# account1.deposite(withdraw_amm)

# deposite_amm2 = input('enter another amount to withdraw')
# account1.deposite(deposite_amm2)
# account1.display()



# 540
# class ATM:  
#         def __init__(self):
#             self.pin = ''
#             self.balance = 0
#             self.menu()

#         def menu(self):
#             print('1. create pin')
#             print('2. change pin')
#             print('3. check balance')
#             print('4. withdraw money')
#             print('5. deposite money')
#             print('6. exit')

#             choice = input('enter your choice: ')

#             if choice == '1':
#                 self.create_pin()        
#             elif choice == '2':
#                 self.change_pin()
#             elif choice == '3':
#                 self.check_bal()
#             elif choice == '4':
#                 self.deposite()
#             elif choice == '5':
#                 self.withdraw()
#             else:
#                 exit()
            
#         def create_pin(self):
#             user_pin = input('enter pin: ')
#             self.pin = user_pin
#             b = int(input('enter bal: ')) 
#             self.bal = b
#             print('pin crearted sucessfully') 
#             self.menu()

#         def change_pin(self):
#             p = input('enter pin: ') 
#             if self.pin == p:
#                 new_pin = input('enter new pin: ')
#                 self.pin = new_pin
#                 print('pin changed sucessfully: ') 
#             else:
#                 print('enter correct pin')
#             self.menu()     
    
#         def check_bal(self):
#             p = input('enter pin')
#             if self.pin == p:
#                 print('your bal: ', self.bal)
#             else:
#                 print('enter correct pin')
#             self.menu()
        
#         def withdraw(self):
#             p = input('enter pin')
#             if self.pin == p:
#                 a = int(input('enter amount you want to withdraw: '))
#                 if a<self.bal:
#                     self.bal -= a
#                     print('balance after withdraw: ',self.bal)
#                 else:
#                     print('enter correct pin') 
#             self.menu()       

# user1 = ATM()

# 539
class sq:
    def __init__(self,l):
        self.l = l
    def shift(self):
        if len(self.l == 0):
            pass
            raise Exception('list is empty')
        try:
            self.l.loop(0)
            print(x)
        except Exception as e:
            print(e)
        
    def unshift(self):
        self.l.insert(0,n)
    def push(self):
        self.l.append(n)
    def pop(self):
        if len(self.l) == 0:
            pass
            raise Exception('list is empty')
        try:
            x = self.l.pop()
            print(x)
        except Exception as e:
            print(e)

    def display(self):
        print(self.l)

l1 = sq([1,2,3,4,5])
l1.shift()
l1.displa()