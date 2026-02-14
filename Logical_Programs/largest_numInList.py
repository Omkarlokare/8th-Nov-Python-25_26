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