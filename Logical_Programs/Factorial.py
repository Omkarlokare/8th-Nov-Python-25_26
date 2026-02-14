print("----Factorial Number")

num=4   #4*3*2*1  1*2*3*4= 24

fact=1     #24
for i in range(1,num+1):  #5<5
    fact=fact*i   #1*1  = 1*2=2*3=6*4=24

print(fact)
print("Factorial of given number",num, "is ",fact)