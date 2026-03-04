list1 = [20,10,30,100,50]
print(list1)
print(type(list1))
print(len(list1))


print("--Print specific number from list--")

print(list1[2])


print("--Print list in reverse order--")

for i in list1[::-1]:
    print(i)


ls = ["Om", 10, 20, "A+", 10]

ls.append("Lokare")
print(ls)

ls.extend(["Hi", 100])
print(ls)

ls.insert(0,"Hello")
print(ls)

ls.pop()
print(ls)

ls.pop(6)
print(ls)

ls.remove("Hi")
print(ls)

ls.reverse()
print(ls)

print(ls.count(10))
