print("----Fibonacci series----")

a = 0
b = 1

for i in range(10):
    print(a, end=" ")
    a, b = b, a+b    # 0 = 1, 0 + 1 = 1
    # print(a)