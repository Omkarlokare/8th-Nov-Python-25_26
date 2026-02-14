# dictionary

dict = { "Name" : "Omkar", "Num": 10, 101 : 100}
print(dict)
print(type(dict))
print(len(dict))


# Print value using key
print("---")
print(dict["Num"])

# add key and value
print("---")
dict["Address"] = "ABC"
print(dict)

# Update value of existing key
dict["Address"] = "DEF"
print(dict)


# Pop K-V pair
dict.pop("Name")
print(dict)

# Remove K-V pair
dict.popitem()
print(dict)

# Check K-V
print("Address" in dict)
print("Num" in dict)

# Print only keys from dict
print("---")
for key in dict.keys():
    print(key)

# print all values
print("---")
print(dict.values())

print("---")
for value in dict.values():
    print(value)


#print all keys and values
print(dict.items())

print("---")
for key,value in dict.items():
    print(key,":",value)
