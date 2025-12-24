# abstraction

from abc import ABC , abstractmethod

# class car(ABC):
#     @abstractmethod
#     def mileage(self):
#         print('min 100')

# class tesla(car):
#     def mileage(self):
#         print('200')

# class maruti(car):
#     def mileage(self):
#         print('30')

# c = car()
# c.mileage()
# t = tesla()


# 657
class employee:
    def get_details(self):
        self.id = input('enter mail id: ')
        self.name = input('enter name: ')
        self.salary = int(input('enter basic salary: '))
    
    def print_detail(self):
        print('name:' , self.name , 'id:',self.id , 'salary:',self.salary)

    def get_salary(self):
        return self.salary
    
    @abstractmethod
    def emp_id(self):
        pass

class perks(employee):
    def calperk(self):
        self.get_details()
        a = self.get_salary()
        self.da = 0.35*a
        self.hra = 0.17*a
        self.pf = 0.12*a

    def putperks(self):
        self.print_detail()
        print('da:',self.da,'hra:',self.hra,'pf:',self.pf)

    def total_perks(self):
        return self.da + self.hra-self.pf
    
    def emp_id(self):
        pass

class netSalary(perks):
    def get_total(self):
        self.calperk()
        self.ns = self.get_salary() + self.total_perks()

    def showTotal(self):
        self.putperks()
        print('total salary:',self.ns)

emp1 = netSalary()
emp1.get_total()
emp1.showTotal()