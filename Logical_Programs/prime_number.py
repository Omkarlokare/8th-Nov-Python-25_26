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




print("----Prime numbers in given range range----")

for num in range(2, 101, 1):
    count = 0

    for i in range(1, num + 1):

        if num % i == 0:
            count = count + 1

    if count == 2:
        print(num)