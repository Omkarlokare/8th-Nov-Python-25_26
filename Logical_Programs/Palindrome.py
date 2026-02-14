print("----Palindrome----")

word = "hello"
rev = ""
for i in word:
    rev = i + rev

if word == rev:
    print("palindrome")
else:
    print("Not palindrome")