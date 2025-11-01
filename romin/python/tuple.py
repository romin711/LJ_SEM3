t1 = (1 , 2, 5.6 , 3 , 'romin' , "abc" , ('a' , 7 , "b"))
# print(type(t1))
# print(t1)

t2 = ('hello')
# print(type(t2))

t3 = ('hello' ,)
# print(type(t3))

t4 = ('hello')
# print(tuple(t4))

# t1[0] = 5
# print(t1)
# del t1[0]

# print(t1[2])
# print(t1[-3])
# print(t1[-1][1])
# print(t1[3][-1::-1])
# print(t1[1:-1:1])
# print(t1[-2:2-1])
# print(t1[-2::])
# print(t1[-2:2:])

t5 = (5 , 6 , 7)
# print(t1 + t5)
# print(t5*2)
# print(t5 in t2)
# print(tuple(range(10 , 20 , 2)))
# print((1,2,3) == (3,2,1))
# print(('A' , 'B') == (65 , 66))
# print(len(t1))
# print(min(t1))
# print(min(t5))
# print(max(t5))
# print(sum(t5))

t6 = ('a' , 'b')
# print(max(t6))

t7 = (10 , 20 , 10 , 10 , 20 , 30 , 10)
# print(t7.count(10))
# print(t7.index(10))
# print(t7.index(30))

# print(sorted(t7))
# print(sorted(t7 , reverse = True))

t8 = (10 , 20 , 30)
a,b,c, = t8
# print(a)
# print(b)
# print(c)

# for i in t8:
    # print(i)
# for i , j in enumerate(t8):
    # print(i , '-' , j)

# wap sum of odd numbers and sum of even numbers from tuple enrtered by user

# sum = eval(input('Enter tuple: '))

# even_sum = 0
# odd_sum = 0

# for i in sum:
#     if i % 2 == 0:
#         even_sum = even_sum + i
#     else:
#         odd_sum = odd_sum + i
# print('sum of even numbers: ' , even_sum)
# print('sum of odd numbers: ' , odd_sum)

# wap to get output as per given case 
# INPUT --> 'This is a python'
# OUTPUT --> 'ThiS IS A PythoN'
# change = input('enter string: ')
# words = change.split()

# print(words)

# w = ' '
# for i in words:
#     if len(i)>1:
#         w += i[0].upper() + i[1:-1].lower() + i[-1].upper() + ' '
#     else:
#         w += i.upper() + ' '
# print(w)



# S = input('Enter String: ')
# shift = int(input('Enter shift Count: '))
# alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# S = S.upper()
# result = ''
# for i in S:
#     if i in alpha:
#         letter_ind = (alpha.find(i) + shift)%len(alpha)
#         result+= alpha[letter_ind]
#     else:
#         result+=i
# print(result)


# wap to encrypt msg as per given shift key(pb question)
s = input('enter string: ')
shift = int(input('enter shift: '))
s1 = ' '
for i in range(shift):
    s1 += s[i::shift]
print(s1)
