s1="velocity"
s2="ABCD"
s3="abcd"
s4=" hi "
s5="my name is abc"
s6="abcaba"


print(len(s1))
print(s1.upper())
print(s2.lower())

print("---------")

print(s2 == s3)
print(s2.__eq__(s3))
print(s2.lower() == s3.lower())

print("--------------")

print("vel" in s1)
print(s1.__contains__("vel"))
print(s1.startswith("vel"))
print(s1.endswith("ty"))

print("-------------")
print(s1[1])
print(s1[2:5])
print(s1.find("i"))
print(s1.rfind("b"))
print(s6.index("c"))

print("--------------------")
print(s1+s2)
print(s4.strip())
print(s4.rstrip())
print(s4.lstrip())
print(s5.replace("abc","xyz"))

print("-----------")
str3="Abcd"

print(str3.swapcase())

print("---------------")
str1="velocity"
str4="122"
str5="abc123"
str6="     "
str7="my name is abc my"
print(str1.isalpha())
print(str4.isdigit())
print(str5.isalnum())
print(str6.isspace())
print(str7.count("my"))       # Occurrence of same word

