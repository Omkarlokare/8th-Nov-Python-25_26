
# Set
set1 = {"Hello", 10, 20, 30, 10}
print(set1)
print(type(set1))
print(len(set1))
# print(set1[0])

# adding elements
print("----")
set1.add("Hey")
print(set1)

# Update elements
set1.update([100,2000])
print(set1)

# remove element
set1.remove("Hey")
print(set1)

# discard element
set1.discard("hi")
set1.discard("Hello")
print(set1)

# Pop
set1.pop()
print(set1)

# copy set
print("-----")
set2 = set1.copy()
print(set2)

# Sort set
# print("-----")
# sortedSet = sorted(set1)
# print(sortedSet)

# search and count
print("----")
print(10 in set1)

# clear
# print("----")
# set1.clear()
# print(set1)

conv = list(set1)
print(conv)

print("-----")
rev = list(set1)
print(rev)

rev.reverse()
print(rev)

