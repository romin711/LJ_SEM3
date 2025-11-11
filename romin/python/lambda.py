s = lambda x : x**2
# print(s(5))

s1 = lambda x,y : x + y
# print(s1(10,20))

s2 = lambda x,y,z : x + (y+z)
# print(s2(y=52 , x = 10 , z = 2))

s4 = lambda s : s in 'LJ KU'
# print(s4('LK'))


l = [1,2,3,4,5]
# print(list(map(lambda x : x**2 , l))) 

l1 = [1,2,3,4,5]
l2 = [10,20,30,40,50]
# print(list(map(lambda x,y : x + y , l1 , l2)))

# print(list(map(lambda x : 'e' if x%2 == 0 else 'o' , l)))

# print(list(filter(lambda x : x%2 == 0 , l)))

f = ['apple' , 'banana' , 'kiwi' , 'orange']
# print(list(filter(lambda x : x.startswith('a') , f)))

# wap to find sum of +ve integers and sum of -ve integers using lambda function
l2 = [1 , -1 , 3 , -6 , -13 , 8]
# print(sum(list(filter(lambda x : x>0, l2))))
# print(sum(list(filter(lambda y : y<0, l2))))



from functools import reduce
l = [1,2,3,4,5]

# print(reduce(lambda x,y : x * y , l))
# print(reduce(lambda x,y : x if x>y else y, l))

users = [{'name' : 'rahul' , 'age ' : 45},
         {'name' : 'raj' , 'age' : 30}]
# print(list(map(lambda x : x['name'] , users)))


l = [10,5,8,7,12]
# print(sorted(l))

d = {4:'a' , 2:'c' , 3:'b'}
# print(sorted(d.items()))

l = sorted(d.items() , key=lambda x:x[1])
# print(dict(l))

l1 = ['ab' , 'abcd' , 'acb']
# print(sorted(l1 , key=len , reverse=True))

# wap to find total number of gifts given to employess as per there rank. higher rank emp will get more gifts than his neighbours 
l = [1,2,3,2,1,4]
n = len(l)
gifts = [1]
for i in range(1,n):
    if l[i] > l[i-1]:
        gifts.append(gifts[i-1] + 1)
    else:
        gifts.append(1)
for i in range(n-2,-1,-1):
    # print(i)
    if l[1] > l[i+1]:
        gifts[i] = max(1+gifts[i+1] , gifts[i])
print(gifts)
print(sum(gifts))