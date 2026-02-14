# Square of 1 - 100 numbers
print("Square of 1 - 50 numbers")
for i in range(1,51):
    square = i**2
    print(square)


# Check if the year is leap or not

print("----------------------------------")
print("Check if the year is leap or not")
year = 1900

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(year, "is a leap year")

else:
    print(year, "is not a leap year")


# Reverse a list
print("--------------------------------")
print("Reverse a list")

ls = [10,20,30,40,50]
reversed_list = []

for i in ls[::-1]:
    reversed_list.append(i)
    # print(reversed_list)
print(reversed_list)
# print(list(reversed(ls)))


# Reverse string
print("-----------------------------")
print("Reverse a string")

string = "hello world"
reversed_string = ""

for i in string:
    reversed_string = i + reversed_string
    # print(result,end="")
    # print(i)
print(reversed_string)


# Reverse string on the same place
print("-----------------------------------")
print("Reverse a string on the same place")

text = "hello world"
split_text = text.split()

reversed_text = [word[::-1] for word in split_text]

result = " ".join(reversed_text)
print(result)


# Fibonacci series
print("--------------------------")
print("Fibonacci series")

a = 0
b = 1

for i in range(10):
    print(a)
    a, b = b, a+b    # 0 = 1, 0 + 1 = 1
    # print(a)

# Prime number
print("-----------------")
print("Prime numbers")

for num in range(2,101,1):
    count = 0

    for i in range(1,num+1):

        if num % i == 0:
            count = count + 1

    if count == 2:
        print(num)


print("-------------------")
# Find duplicate in a list
print("Find duplicate in a list")

ls = [1,2,3,4,5,6,6,7,3,2]

seen = []
dup = []

for i in ls:
    if i in seen:
        dup.append(i)
    else:
        seen.append(i)
print("List without duplicates:", seen)
print("Duplicates in a list:", dup)


print("---------------------")
print("Anagram:")

def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)

print(is_anagram("hello", "world"))
print(is_anagram("silent", "listen"))


# Check the string is palindrome or not

print("---------------------")
print("Palindrome")


def is_palindrome(word):
    rev = ""
    for i in word:
        rev = i + rev
    return rev == word

print(is_palindrome("lool"))


# Find the largest of three numbers
print("----------------------")
print("Largest number in list")


# def is_large(num1,num2,num3):
#
#     if num1 > num2 and num1 > num3:
#         # print(num1,"Is the greater number")
#         return num1
#     elif num2 > num1 and num2 > num3:
#         # print(num2,"Is the greater number")
#         return num2
#     elif num3 > num1 and num3 > num2:
#         # print(num3,"Is the greater number")
#         return num3
#     else:
#         print("Invalid input")
#
# a = is_large(int(input("Enter a number 1: ")),int(input("Enter a number 2: ")),int(input("Enter a number 3: ")))
# print(a,"Is the greatest number")



# Swap variables
print("--------------")
print("Swap variables")

x = 10
y = 5

x,y = y,x

print("x=",x,"y=",y)

print("------------")

a = 5
b = 10
c = a    # c = 5
a = b    # a = 10
b = c    # b = 5
print("a=",a, "b=",b)


# Check Armstrong number
print("Check Armstrong number")

# num = int(input("Enter a number: "))
#
# temp = num
# sum = 0
# digits = len(str(num))
#
# while temp > 0:
#     digit = temp % 10
#     sum = sum + digit ** digits
#     temp = temp // 10
#
# if sum == num:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")



