# a = input("Enter a letter: ")
#
# if a in "aeiouAEIOU":
#     print("This is vowel")
#
# else:
#     print("This is consonant")


print("----check prime numb----")

num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")

else:
    is_Prime = True

    for i in range(2, num):
        if num % i == 0:
            is_Prime = False
            break

    if is_Prime:
        print("Prime number")

    else:
        print("Not a prime number")






