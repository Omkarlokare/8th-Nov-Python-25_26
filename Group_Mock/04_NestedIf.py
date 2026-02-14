
age = float(input("Enter age: "))


if age >= 18:
    print("Client is an adult")

    age2 = age
    if age2 >= 25:
        print("Client is allowed to have alcohol")

    else:
        print("Client is an adult but not allowed to have alcohol")

else:
    print("Client is a minor")


