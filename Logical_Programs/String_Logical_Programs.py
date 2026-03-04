# print("----Find a largest word in a sentence----")
#
# sentence = input("Enter a sentence: ")
#
# words = sentence.split()
# print(words)  # ['i', 'am', 'a', 'good', 'python', 'coder']
# largest_word = words[0]
#
# for word in words:
#     if len(word) > len(largest_word):
#         largest_word = word
#
# print("Largest word:", largest_word)
# print("Length:", len(largest_word))



# WAP to find duplicates in a string

inp = input("Enter a String: ")

# inp = inp.lower()
# inp = inp.upper()

# inp = inp.replace(" ","")

dup = {}

for i in inp:
    if i in dup:
        dup[i]=dup[i]+1
    else:
        dup[i]=1
print("Duplicates are: ")
for i in dup:
    if dup[i]>1:
        print(i,end=" ")

# print("----------------------")


#Wap to find first non-repeating character in a String


# s = input("Enter a string: ")
#
# freq = {}
#
# for char in s:
#     if char in freq:
#         freq[char] += 1
#
#     else:
#         freq[char] = 1
#
# print("Non Repetitive Elements are: ")
#
# for i in s:
#     if freq[i]==1:
#         print(i,end="")


# print("----------------------")


#WAP to remove Duplicates in a String.

# inp1 = input("Enter a Sentence: ")
#
# dup = ""
#
# for i in inp1:
#     if i not in dup:
#         dup = dup + i
# print("Non Duplicates are: ",dup)
#
# print()
#
# print("----------------------")
#
#
# #WAP replace space with -
#
# s = input("Enter a Sentence: ")
#
# s1 = s.replace(" ","-")
#
# print(s1)