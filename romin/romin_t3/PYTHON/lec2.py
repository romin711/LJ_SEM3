# 466
# f = open('city.txt' , 'w+')
# f.writelines(['ahmedabad\nbhavnagar' ])
# f.seek(0)
# s = f.read()
# print(s)
# f.close()



# 469
# file = open("469.txt", "r")
# text = file.read()
# file.close()

# words = text.split()
# print("number of words:", len(words))

# sentences = text.split(".")
# print("number of sentences:", len(sentences) - 1)


# 470
# file = open("469.txt", "r") 
# text = file.read()

# text = text.upper()
# file = open('469.txt' , 'w')
# file.write(text)

# file.close()


# 471
# file = open("469.txt", "r") 
# text = file.read()

# text = text.upper()
# file = open('470(a).txt' , 'w')
# file.write(text)

# file.close()


# 472
# f1 = open('fileA.txt' , 'r')
# f2 = open('fileB.txt' , 'r')

# f3 = open('fileC.txt' , 'w')

# l1 = f1.readlines()
# l2 = f2.readlines()


# l = max(len(l1) , len(l2))

# for i in range(l):
#     if len(l1) > i:
#         f3.write(l1[i])

#     if len(l2) > i:
#         f3.write(l2[i])

# f3 = open('fileC.txt')
# s = f3.read()
# print(s)

# f1.close()
# f2.close()
# f3.close()

# 474
# user_word = input('enter word: ')
# f = open('469.txt')
# l = f.readlines()

# for i in l:
#     if i.find(user_word)!=1:
#         print('line no=' , l.index(i)+1 , 'index no=' , i.index(user_word))



# 475
# f = open(input('enter file name: '))

# for i , j in enumerate(f):
#     if i % 25 == 0 and i:
#         x = input('do you want to continue? enter y or n:')
#         if x.lower() == "n":
#             break
#     else:
#         print(j)



# 476

# f1 = open("abc1.txt", "r")
# f2 = open("abc2.txt", "w")
# for i in f1:
#     reversed_line = i[::-1]
#     f2.write(reversed_line)   
#     print(reversed_line)
# f1.close()
# f2.close()


# f2 = open("abc1.txt", "r")
# f3 = open("abc2.txt", "w")
# for j in f2:
#     upper_line = j.upper()
#     f3.write(upper_line)
#     print(upper_line)

# f2.close()
# f3.close()


# 483
# f = open('mbox-short.txt' , encoding="utf-8")
# # print(f.read())

# l = []
# d = {}

# for i in f:
#     if not i.startswith('From '):
#         continue
#     w = i.split()
#     l.append(w[1])

# for i in l:
#     d[i] = d.get(i,0)+1
# print(d)

# a = max(d.values())
# for k,v in d.items():
#     if a==v:
#         print(k,v)



# 480
f = open("file1.txt")
f1 = open("file1.txt" , 'w')

while True:
    b = f.readline()
    if len(b) != 0:
        if b[0]=="#":
            continue
        else:
            if '#' in b:
                for i in range(1 , len(b)):
                    if b[i] == '#':
                        f1.write(b[:i] + '\n')
            else:
                f1.write(b)
    else:
        break
f.close()
f1.close()
f2 = open("file2.txt")
print(f2.read())
f2.close()