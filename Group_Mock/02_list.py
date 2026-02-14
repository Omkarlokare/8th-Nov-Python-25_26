# list

list1 = [10,100,20,120,50]
#         |  |   |   |  |
#         0  1   2   3  4

print(list1)
print(type(list1))

print(len(list1))

# Append
print("--Append--")
list1.append("Hi")
print(list1)
print(len(list1))

print("--Insert--")
list1.insert(2, "Hello")
print(list1)

print("--Extend--")
list1.extend([101,110])
print(list1)

print("--Pop--")
list1.pop()
print(list1)

list1.pop(2)
print(list1)

print("--Remove--")
list1.remove("Hi")
print(list1)

print("--Copy--")
list2 = list1.copy()
print(list2)

print("----")
print(list1)
print(list2)



print("--Reverse--")
list2.reverse()
print(list2)

# list1.extend(["Hello", "Hi"])
list1.insert(2, 10)
# print(list1)

print("--sort--")
list1.sort()
print(list1)

print("--Count--")
count = list1.count(10)
print(count)

print("--Clear--")
list1.clear()
print(list1)

