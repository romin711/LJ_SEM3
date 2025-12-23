# class shapes:
#     def shapes(self):
#         print('shapes')

# class triangle:
#     def triangle(self):
#         print('triangle')

# class square(triangle, shapes):
#     def square(self):
#         print('square')

# S = square()

# S.shapes()
# S.triangle()
# S.square()






# 632
# class book:
#     def __init__(self, name, author, publication, year):
#         self.name = name        
#         self.author = author        
#         self.publication = publication        
#         self.year = year 

#     def display(self):
#         print(self.name , self.author, self.publication, self.year) 

# class courseBook(book):
#     def __init__(self, name, author, publication, year , course):
#         super().__init__(name , author , publication , year)
#         self.course = course
#         # super().self.name

#     def display(self):
#         super().display()      
#         print(self.course)

# obj = courseBook('py1' , 'rao' , 'tata' , '2013' , 'ce')
# obj.display()







# 641
class student:
    def __init__(self , name , roll_no , marks , age):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        self.age = age

    def __eq__(self, other):
        return self.marks == other.marks

s1 = student('raj' , 12 , 99 , 20)
s2 = student('khushi' , 11 , 100 ,21)
if s1 == s2:
    print('same marks')
else:
    print('not same marks')