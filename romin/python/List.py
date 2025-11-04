# l = [1 ,2 ,3 , 'abc' , (11,12,13) , [61 , 62]]
# l1 = []
# l2 = list('hello')
# l3 = list(('hello',))

# print(type(l1))
# print(l , l2 ,l3)
# print(l[-1])
# print(l[-2][1:3])
# print(l[1:-1][2][-1])
# print(l[-1::-2][1][1])

# ---------------------------------------------------------------

# ls = [1 ,2 , 3 , [1,2] , 'abcd']
# print(ls[-1:-3:-1][-1][-2])
# l1 = [1 , 2 , 3 , 4]
# l2 = [[1 , 2] , [3 , 4]]
# l3 = [[[1 , 2] , [3 , 4]] , [[5 , 6] , [7 , 8]]]

# print(l1[2])
# print(l2[1][0])
# print(l3[1][0][1])

# ----------------------------------------------------------------

l = [1 ,2 ,3 , 4]
# l.append(5)
# print(l)

# l.append(['a' 'b'])
# print(l)

# l.append('c' , 'd')

# l = [1 , 2 , 3 , 4]
# l.extend(['c' , 'd'])
# print(l)

# l1 = [6 , 7 , 8]
# l2 = [9 , 10]
# l1.extend(l2)
# print(l1)
# l2.extend(l1)
# print(l2)

# l.insert(1,100)
# print(l)


# -----------------------------------------------------------------

# l = [1 , 2 , 3 , 4]
# del l[-1] 
# del l[1:]
# print(l)

# l1 = [1 , 2 , 2 , 1 , 3 , 2 , 5 , 2]
# l1.remove(2)
# l1.remove(2)
# print(l1)

# l1.pop()
# print(l1)
# l1.pop(3)
# print(l1)

# l = [1 , 2 , 3]
# l.clear()
# print(l)

# ------------------------------------------------------------------

# l1 = [1 , 2 , 3 , 4]
# l2 = [5 ,6]

# print(l1 + l2)
# print(l2*5)
# print(2 in l1)
# print([1,2,3] == [3,2,1])
# print(['a'] + ['b'])

# for i in l1:
#     print(i)
# for i,j in enumerate(l1):
#     print(i , ' - ' , j)

# -------------------------------------------------------

# l = [[1,2] , [3 , 4]]

# for i in l:
#     print(i)
#     for j in i:
#         print(j)


# -------------------------------------------------------

# l1 = [1, 2 , 3 , 4]
# print(len(l1))
# print(sum(l1))
# print(min(l1))
# print(max(l1))

# print(sum(['a' , '12']))
# print(min(['a' , '12']))

# l = [1 , 2 , 2 ,1 , 3 , 2]
# # print(l.count(2))
# # l.reverse()
# # print(l)

# l2 = [11 , 2 , 6 , 13 , 9 ]
# l2.sort()
# print(l2)

# l3 = [11 ,2 , 6 ,13, 9]
# print(sorted(l3))
# print(sorted(l3 , reverse=True))

# l4 = [1 , 2 , 2 , 3 , 5 , 2 , 1]
# print(l4.index(2))
# print(l4.index(2,3,7))

# -----------------------------------
# l1 = [ 1,2,3,4]
# l2 = l1

# print(id(l1))
# print(id(l2))

# ----------------------------

# wap to generate list with 10 elements 1-10
# l = []
# for i in range(1,11):
#     l.append(i)
# print(l)

# print([i for i in range (1,11) if i % 2 == 0])


# wap to display list elements from 1 -51 divisable by 5 using lis tcomprehension
# print([i for i in range (1,52) if i % 5 == 0])

# wap common name of fruit which start with a
# fruit_list_1 = ['apple' , 'banana' , 'cherry' , 'kiwi'] 
# fruit_list_2 = ['cherry' , 'grapes' , 'apple' , 'orange'] 

# print([i for i in fruit_list_1 if i in fruit_list_2 if i[0] == 'a'])

# wap to print a list after performing running sum on it
# list = [1,2,3,4,5]
# sum_list =[]

# total = 0

# for i in list:
#     total = total + i
#     sum_list.append(total)
# print(sum_list)

# --------------------------------------------------------

# l = [2 , 4 , 6 , 10 , 1]

# new_l = []

# for i in l:
#     s = 0
#     for j in l:
#         if i <= j:
#             s = s + j
#     new_l.append(s)
# print(new_l)

