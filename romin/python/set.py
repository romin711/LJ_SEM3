# mutable,  unordered , no duplicate elemets allowed , {} , 

s = {1,2,3}
# print(type(s))

s1 = {}
# print(type(s1))

s2 = set()
# print(type(s2))

# print({1,2,3} == {3,2,1})

s3 = {1,1,2,2,2,3}
# print(s3)

# s4 = {[1,2,3] , 4,5}
# print(s4)

s5 = {(1,2,3), 3 , 4 , 'ab'}
# print(s5)

s.add(4)
# print(s)

s.update(['a' , 'b' , 'c'])
# print(s)

name = {'romin' , 'prince' , 'jenish'}
# print(sorted(name , reverse=False))

# num1 = {1,2,3,4,5,6}
# num2 = {7,2,10,6,3}

# print(num1)
# print(num2)

random_num = {100, 1, 50, 3, 2}
# print(sorted(random_num , reverse=False))
# s.pop()
# print(s)
# s.clear()
# print(s)

# operation of set::
# s1 = {1,2,3,4,5}
# s1 = {4,5,6,7,8,9}

# print(s1 | s2)
# print(s1.union(s2))
# print(s1 & s2)
# print(s1.intersection(s2))
# print(s1-s2)
# print(s1.difference(s2))
# print(s2-s1)
# print(s1^s2)
# print(s1.symmetric_difference(s2))

# s6 = {1,2,3,4,5,6}
# print(len(s6))
# print(min(s6))
# print(max(s6))
# print(sum(s6))

# s7 = {1,2,3,4}
# s8 = {1,2}

# print(s7.issuperset(s8))
# print(s8.issubset(s7))


# # set comprehension

# print({i**2 for i in range(1,11)})
# print((i**2 for i in range(1,11)))

# a = ['a' , 'b' , 'c' , 'd']
# s9 = reversed(a)
# print(s9)
# print(list(s9))
# print(list(reversed('hello')))

# wap to convert entered intger number by user into word(from 0 to 999) 
# def int_to_words(n):
#     d = {
#     0: 'zero ',
#     1: 'one ',
#     2: 'two ',
#     3: 'three ',
#     4: 'four ',
#     5: 'five ',
#     6: 'six ',
#     7: 'seven ',
#     8: 'eight ',
#     9: 'nine ',
#     10: 'ten ',
#     11: 'eleven ',
#     12: 'twelve ',
#     13: 'thirteen ',
#     14: 'fourteen ',
#     15: 'fifteen ',
#     16: 'sixteen ',
#     17: 'seventeen ',
#     18: 'eighteen ',
#     19: 'nineteen ',
#     20: 'twenty ',
#     30: 'thirty ',
#     40: 'forty ',
#     50: 'fifty ',
#     60: 'sixty ',
#     70: 'seventy ',
#     80: 'eighty ',
#     90: 'ninety '    
#     }

#     if n < 20:
#         return d[n]
#     if n >= 20 and n < 100:
#         if n % 10 == 0:
#             return d[n]
#         else:
#             return d[n//10 * 10] + ' ' + d[n % 10]
#     if n >= 100 and n < 1000:
#         if n % 100 == 0:
#             return d[n//100] + 'hundred '
#         else:
#             return d[n//100] + 'hundred ' + int_to_words(n%100)

# n = int(input('enter no : '))
# print(int_to_words(n))


# wap to find common prefix from the given list 
# l = ['lessonplan' , 'length' , 'less']
# l.sort()
# print(l)
# end = min(len(l[0]) , len(l[-1]))
# print(end)
# s = " "
# i = 0

# while i < end and l[0][i] == l[-1][i]:
#     s = s + l[0][i]
#     i = i + 1
# if s == ' ':
#     print(-1)
# else:
#     print(s)



n = int(input("Enter the size of the matrix (n): "))

matrix = []

print("Enter the matrix row by row:")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(n):
    for j in range(i, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

for row in matrix:
    row.reverse()

print("Rotated matrix:")
for row in matrix:
    print(" ".join(map(str, row)))


