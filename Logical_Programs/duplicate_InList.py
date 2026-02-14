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