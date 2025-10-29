a = "my self romin kevadiya!!"

# print(a[0])
# print(a[-2])
# print(a[0:24:2])
# print(a[-1:-25:-1])

# a[0] = 'x'
# print(a)

# del a
# print(a)

# s1 = "lj"
# s2 = "university"
# print(s1*2)

# logical
# print('hello' or 'hi')
# print('' or 'hi')
# print('hello' and '')


# print(not 'hello')
# print('he' in 'hello')
# print('he' not in 'hello')
# print('hello' < 'hi')
# print('h' == 'h')

# s = 'students'
# print(id(s))
# s += 'romin'
# print(id(s))


# s='hello students'
# for i in s:
#     print(i , end="" )
# for i,j in enumerate(s):
#     print(i , '-' , j)


# m = input('Enter string: ')
# b = m[::-1]
# if m == b:
#     print('same')  
# else:
#     print('not same') 


# m = input("enter a string: ")

# first = m[0]
# last = m[-1]
# middle_index = len(m)// 2
# middle = m[middle_index]

# print("First character:", first)
# print("Middle character:", middle)
# print("Last character:", last)


c = 'kevadiya romin'
c1 = 'romin007'
# print(len(c))
# print(max(c))
# print(min(c))
# print(sorted(c))
# print(sorted(c , reverse = True))
# print(c.capitalize())
# print(c.title())
# print(c.upper())
# print(c.lower())
# print(c.swapcase())
# print(c.count('a'))
# print(dir(c))

# print(c1.isalnum())
# print(c.isalnum())
# print(c.isalpha())
# print(' '.isspace())
# print('007'.isdigit())
# print('007'.isnumeric())
# print('romin007'.istitle())
# print(c.isupper())
# print(c.islower())

p1 = 'learning python is easy in programming'
# print(p1.find('in'))
# print(p1.rfind('in'))
# print(p1.find('in' , 15 , len(p1)))
# print(p1.rfind('in' , 15 , len(p1)))
# print(p1.find('xyz'))
# print(p1.index('in'))
# print(p1.rindex('in'))
# print(p1.index('in' , 15 , len(p1)))
# print(p1.rindex('in' , 15 , len(p1)))
# print(len(p1))
# print(p1.index('xyz'))

# print(" ".join(['hi' , 'my' , 'world']))
# print("<".join('123'))

# print(p1.split())
# print(p1.split('in'))

# print(p1.replace('in' , 'of'))
# print(p1.replace('in' , 'of' , 2))

# print('abcxyzbca'.strip('a'))
# print('abcxyzbca'.lstrip('a'))
# print('abcxyzbca'.rstrip('a'))

# # wap to print even length words from string
# input_str = "This is a simple test string with even and odd words"
# words = input_str.split()

# for word in words:
#     if len(word) % 2 == 0:
#         print(word)


# wap to check wether teo strings are balanced or not. strings are balanced if all characters in s1 are presents in s2.
# s1 = "abc"
# s2 = "agfqb"

# balanc = 1
# for i in s1:
#     if i not in s2:
#         balanc = 0
#         break

# if balanc:
#     print("balanced")
# else:
#     print("not balanced")


# to convert entered string by user into even positions of character in upper case and odd posotion of char in lower case
# user = input("Enter a string: ")
# convert = ""

# for i in range(len(user)):
#     if i % 2 == 0:
#         convert = convert + user[i].upper()
#     else:
#         convert = convert + user[i].lower()

# print("new string:"+ convert)

# # wap to remove vowels from the string and re display string
# str = input("Enter a string: ")
# vowels = "aeiouAEIOU"
# result = ""

# for i in str:
#     if i not in vowels:
#         result = result + i

# print("String after removing vowels:" + result)



# intab = 'aeiou'
# outab = '12345'

# s = 'This is Python'
# t = s.maketrans(intab , outab)
# # print(t)  
# print(s.translate(t))

# import string
# print(string.punctuation)
# a = 'Thi#s ?is/ pyth,o.n'

# new = a.translate(
#     a.maketrans
#     ('' , '' , string.punctuation)
# )
# print(new)

# wap to calculate number of upper case number , lower case , digits and space from the given string
# str = input("Enter a string: ")

# upper = 0
# lower = 0
# digit = 0
# space = 0
# for i in str:
#     if i.isupper():
#         upper += 1
#     elif i.islower():
#         lower += 1
#     elif i.isdigit():
#         digit += 1
#     elif i.isspace():
#         space += 1

# print("Uppercase letters:", upper)
# print("Lowercase letters:", lower)
# print("Digits:", digit)
# print("Spaces:", space)

# wap to check validation of password
# * conditions : 
#            1. min 8 character
#            2. alphabets must [a-z]
#            3. at least 1 uppercase [A-Z]
#            4. at least 1 digit [0-9]
#            5. at least 1 char from [_ , @ , $]
# password = input("Enter a password: ")
# flag = True
# if len(password) >= 8:
#     for i in password:
#         if password.islower():
#             # print('requirenment successfull(contains 1 lower character)')
#             print('')
#         else:
#             print('password must contain lowercase')
#         if password.isupper():
#             # print('requirenment successfull(contains 1 upper character)')
#             print('')
#         else:
#             print('password must contain uppercase')
#         if password.isdigit():
#             # print('requirenment successfull(contains 1 digit)')
#             print('')
#         else:
#             print('password must contain digit')
#         if i == '@' or i == '_' or i == '$':
#             print('password successfull')
#             print('')
#         else:
#             print('password must contain $ @ _')
#             break
# else:
#     print('length must be greater than ')

# wap using function to shift the decimal digit and places to the left, wraping th extra digits around. if shift > the number of digits of number than reverse the number
# def shifting(n , shift) :
#     str_num = str(number)
    
#     if shift > len(str_num):
#         result = str_num[::-1]
#     else:
#         result = str_num[shift:] + str_num[:shift]
#     return int(result)

# number = int(input('enter number:'))
# shift_num = int(input('enter shift number:'))

# print(shifting(number , shift_num))


# upper to lower , lower to upper of string
text = input("Enter a string: ")
new = ""
for i in text:
    if i.isupper():
        new += i.lower()
    elif i.islower():
        new += i.upper()
    else:
        new += i 

print("String after flipping case:", new)

print(text.swapcase())
