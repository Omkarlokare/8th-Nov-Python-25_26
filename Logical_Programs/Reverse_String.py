print("----Reverse string")

str = input("Enter a string: ")

rev_str = ""

for i in str:
    rev_str = i + rev_str

print(rev_str)

print("----Reverse sentence with same word----")

inp = "Python and data science"

sp = inp.split()

rev = sp[::-1]

output = " ".join(rev)
print(output)


print("----Reverse a string on the same place----")

text = "hello world"
split_text = text.split()

reversed_text = [word[::-1] for word in split_text]

result = " ".join(reversed_text)
print(result)