d = {'name' : 'raj' , 'age' : 33 , 'gender' : 'male'} 
# print(d)
# print(type(d))

l = [('a' , 10) , ('b' , 20) , ('c' , 30)]
# print(dict(l))

d1 = {(1,2,3) : 'abc' , 'abc' : 123}
# print(d1)

# d2 = {[1,2,3] : 'abc' , 'a' : 367}
# print(d2)

d3 = {'name' : 'raj' ,
      'branch' : 'ce' ,
      'subject' : {'de' : 25 ,
                   'py' : 24 ,
                   'fsd' : 24 ,
                   'ps' : 23}}
# print(d3['subject'])
d3['branch'] = 'cst'
# print(d3)

d4 = {'a' : 10 , 'a' : 20}
# print(d4['a'])
# print(d4)
# print(d3.get('name'))
# print(d3['subject']['py'])

# ---------------------------------------------------------------------
d3['gender'] = 'male'
# print(d3)

# ---------------------------------------------------------------------
# d3.pop('gender')
# d3.popitem()
# del d3['name']
# print(d3)

dic1 = {'a' : 10 , 'b' : 20}
dic1.clear()
# print(dic1)

# print('name' in d3)
# print('raj' in d3)

dic2 = {'a' : 10 , 'c' : 20 , 'b' : 30}
# for i in dic2:
    # print(i , '-', dic2[i])

# print(len(dic2))
# print(sorted(dic2))
# print(sorted(dic2 , reverse='True'))
# print(max(dic2))
# print(min(dic2))

# print(dic2.keys())
# print(dic2.values())
# print(dic2.items())

# for i , j in dic2.items():
#     print(i , '-' , j)
# dic3 = {'d' : 40 , 'e' : 50}
# dic2.update(dic3)
# print(dic2)

# dic4 = {'a' : 10 , 'b' : 20 , 'c' : 30}
# dic4.setdefault('d' , 40)
# print(dic4)
# dic4.setdefault('d' , 40)
# print(dic4)


# l1 = [1,2,3,4,5]
# l2 = ['a' , 'b' , 'c' , 'd' , 'e' ,'f']
# print(list(zip(l1,l2)))

# ------------------------ dictionary comprehension ------------------------

# print({i:i*i for i in range(1,11)})

l1 = ['s' , 'm' , 't' 'w' 'th' , 'f' , 'sa']
l2 = [30 , 28 , 30 , 29 , 30 , 28 , 30]
# print({i:j for i , j in zip(l1 , l2)})

# str = 'lj best for EC students'
# d = {'best' : 'is best' ,
#      'EC' : 'VLSI'}

# l = []
# for i in str.split():
#     if i in d:
#         l.append(d[i])
#     else:
#         l.append(i)
# print(' '.join(l))

# wap to to count word available in your strings and convert into dictionary
# s = 'abcd acd cdfg jfdf'
# count_wrod = {}
# d = {}
# for i in s.split():
#     d[i[0]] = d.get(i[0] , 0) + 1
# print(d)

# wap to to count letter available in your strings and convert into dictionary
# s = 'abcdefabc'
# d = {}
# for i in s:
#     d[i] = d.get(i , 0) + 1
# print(d)


# ----------------------------------------------
# s = 'abc def ghi ahme surat'
# d = {}

# for i in s.split():
#     if i[0] not in d.keys():   
#         d[i[0]] = []
#         d[i[0]].append(i)
#     else:
        


# wap for a list entered by user with interger number, you need to count the number of special element in the given list , an element is special if removal of that element makes the list balanced. the list will be balanced if sum of even index elements is equal to the sum of odd index elements

l = eval(input('enter integer number: '))
count = 0
for i in range(0 , len(l)):
    c = l.copy()
    c.pop(i)
    s1 = sum(c[0::2])
    s2 = sum(c[1::2])
    if s1 == s2:
        count += 1
print('special element=' , count)