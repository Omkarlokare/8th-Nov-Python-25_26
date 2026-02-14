# print("----Frequency of words in sentence----")
#
# s = input("Enter a string: ")
#
# s1 = s.replace(" ", "")
# print(s1)
#
# freq = {}
#
# for char in s1:
#     if char in freq:
#         freq[char] += 1
#
#     else:
#         freq[char] = 1
#
# print(freq)



s = input("Enter a string: ")

freq = {}

for char in s:
    if char == " ":
        continue          # skip blank spaces

    elif char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print(freq)


# 163108