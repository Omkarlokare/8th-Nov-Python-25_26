import copy

'''-------------------------------------------------------------------------------------'''

print("----Prime number----")
num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")

for i in range(2, num):
    if num % i == 0:
        print("Not a prime number")
        break

else:
    print("Prime number")

'''-------------------------------------------------------------------------------------'''

print("----Prime numbers in given range range----")

for num in range(2, 101, 1):
    count = 0

    for i in range(1, num + 1):

        if num % i == 0:
            count = count + 1

    if count == 2:
        print(num)

'''-------------------------------------------------------------------------------------'''

print("----Second largest number in list----")

lst = []

for i in range(int(input("Enter a number of element: "))):
    x = int(input("Enter a element: "))
    lst.append(x)
print("Actual list",lst)

def m1(lst):
    lst.sort()
    print("Second largest number in a list: ", lst[-2])

m1(lst)

'''-------------------------------------------------------------------------------------'''

print("----Reverse string")

str = input("Enter a string: ")

rev_str = ""

for i in str:
    rev_str = i + rev_str

print(rev_str)

'''------------------------------------------------------------------------------------'''

print("----Reverse string with same word----")

inp = "Python and data science"

sp = inp.split()

rev = sp[::-1]

output = " ".join(rev)
print(output)

'''-------------------------------------------------------------------------------------'''

print("----Duplicate numb in list----")

lst = [1,2,3,4,5,6,2,3]

seen = []
dup = []

for i in lst:
    if i in seen:
        dup.append(i)
    else:
        seen.append(i)

print("List without dupl: ", seen)
print("Duplicates in list: ", dup)

'''------------------------------------------------------------------------------------'''

print("----Reverse List----")

lst1 = [10,20,30,40]

rev_lst = []

for i in lst1[::-1]:
    rev_lst.append(i)

print(rev_lst)

'''-------------------------------------------------------------------------------------'''

print("----Reverse a string on the same place----")

text = "hello world"
split_text = text.split()

reversed_text = [word[::-1] for word in split_text]

result = " ".join(reversed_text)
print(result)


'''--------------------------------------------------------------------------------------'''

print("----Factorial Number")

num=4   #4*3*2*1  1*2*3*4= 24

fact=1     #24
for i in range(1,num+1):  #5<5
    fact=fact*i   #1*1  = 1*2=2*3=6*4=24

print(fact)
print("Factorial of given number",num, "is ",fact)

'''--------------------------------------------------------------------------------------'''

print("----Palindrome----")

word = "hello"
rev = ""
for i in word:
    rev = i + rev

if word == rev:
    print("palindrome")
else:
    print("Not palindrome")


'''-------------------------------------------------------------------------------------'''

print("----Fibonacci series----")

a = 0
b = 1

for i in range(10):
    print(a, end=" ")
    a, b = b, a+b    # 0 = 1, 0 + 1 = 1
    # print(a)


'''----------------------------------------------------------------------------------------'''

print("----Frequency of words in sentence")

s = input("Enter a string: ")

freq = {}

for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print(freq)

'''----------------------------------------------------------------------------------------'''

print("----Find largest and smallest element in a list----")

ls = [10,34,56,22,11,9]

largest = ls[0]
smallest = ls[0]

for i in ls:

    if i > largest:
        largest = i
    if i < smallest:
        smallest = i
print("Largest number is: ",largest)
print("Smallest number is: ",smallest)

'''----------------------------------------------------------------------------------------'''

print("Anagram:")

def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)

print(is_anagram("hello", "world"))
print(is_anagram("silent", "listen"))

'''----------------------------------------------------------------------------------------'''

print("----Swap variables----")

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