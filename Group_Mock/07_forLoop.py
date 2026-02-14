from shlex import split

# reverse list using for loop

list1 = [10,20,30,40,50]

# print(list1[ :  :-1 ]
reversedlist = []

for i in list1[::-1]:
    reversedlist.append(i)

print(reversedlist)

# for i in list1[::-1]:
#     print(i,end=' ')
#
# # print()


# # for i in range(1,6):   #2<6
# #     print(i)                #1 2 3 4 5
#
# print("-----")
#
# for i in range(1,6,1):   #2<6
#     print(i)


# Reverse string
print("----")

string = input("Enter string: ")
reversedString = ""

for i in string[::-1]:
    reversedString = reversedString + i
print(reversedString)

