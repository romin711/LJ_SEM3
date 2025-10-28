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

print(" ".join(['hi' , 'my' , 'world']))
print("<".join('123'))

print(p1.split())
print(p1.split('in'))

print(p1.replace('in' , 'of'))
print(p1.replace('in' , 'of' , 2))

print('abcxyzbca'.strip('a'))
print('abcxyzbca'.lstrip('a'))
print('abcxyzbca'.rstrip('a'))

# wap to print even length words from string
input_str = "This is a simple test string with even and odd words"
words = input_str.split()

for word in words:
    if len(word) % 2 == 0:
        print(word)


# wap to check wether teo strings are balanced or not. strings are balanced if all characters in s1 are presents in s2.
s1 = "abc"
s2 = "agfqbc"

balanc = True
for char in s1:
    if char not in s2:
        balanc = False
        break

if balanc:
    print("balanced")
else:
    print("not balanced")
