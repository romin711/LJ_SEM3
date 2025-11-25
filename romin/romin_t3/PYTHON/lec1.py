# write
# f = open('file1.txt' , 'w')
# f.write('hello , welcome\n')

# f.writelines('jan,\nfeb,\nmarch,\n' )

# f.close()

# append
# f = open('file1.txt' , 'a')
# f.write('hello , welcome\n')

# f.writelines('jan,\nfeb,\nmarch,\n' )

# f.close()

# read mode
# f = open('file1.txt' , 'r')
# s = f.read(8)
# print(s)
# f.close()

# read line
# f = open('file1.txt')
# s = f.readline()
# print(s)
# f.close()

# f2 = open('file1.txt')
# s = f2.readline(2)
# print(s)
# s1 = f2.readline(10)
# print(s1)
# f2.close()


# f3 = open('file1.txt' , 'r')
# s = f3.readlines()
# print(s)
# f3.close()

# f3 = open('file1.txt' , 'r')
# s = f3.readlines(20)
# print(s)
# f3.close()

# f4 = open('file1.txt')
# s = f4.read(4)
# s1 = f4.readline()
# s2 = f4.readline(3)
# s3 = f4.read()
# s4 = f4.readlines()
# print(s4)


# wap to count number of lines from the file
# r1 = open('file1.txt', 'r')
# c = 0
# l = r1.readlines()

# for i in l:
#     if i =='\n':
#         continue
#     else:
#         c = c + 1
# print('no of lines:' ,c)

# s = r1.read()       
# l1 = s.split()
# print(len(l1) , 'Number of words')


# f = open('file1.txt' ,'w')
# print(f.name)
# print(f.mode)
# print(f.readable())
# print(f.writable())
# print(f.closed)
# f.close()
# print(f.closed)

# wap to get odd number of lines from file
# f = open('file2.txt' , 'r')
# l = f.readlines()
# print(l[::2])
# f.close()


# wap to get data from user name , branch , roll number and store in std.txt file

f = open("std.txt", "a")
name = input("Enter your name: ")
branch = input("Enter your branch: ")
roll_number = input("Enter your roll number: ")

f.write("Name: " + name + "\n")
f.write("Branch: " + branch + "\n")
f.write("Roll Number: " + roll_number + "\n")

# Close the file
f.close()

print("Data has been stored in std.txt")
