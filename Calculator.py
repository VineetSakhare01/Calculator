

# Write a program to create  a calculator that can perform at least
# five different maths operations such as addition, substraction, multiplication, division, average.
# Ensure that program is user friendly, prompying for input & displaying results clearly.


a = int(input("Enter first number: "))
b = int(input("Enter Second number: "))
a1 = input("Which mathematical operation do you want to perform  ?:\n \
           1. addition\n\
           2. substraction\n\
           3. multiplication\n\
           4. division\n\
           5. average\n\
           \n\
           ")


def add(a,b):
    c = a+b
    return c

def substract(a,b):
    d = a-b
    return d

def multi(a,b):
    e = a*b
    return e

def divid(a,b):
    x = a/b
    return x

def avg(a,b):
    y = (a+b)/2
    return y


if a1 == "addition":
    z = add(a,b)
    print(f"The Addition of {a} & {b} is {z}.")
elif a1 == "substraction":
    v = substract(a,b)
    print(f"The Substraction of {a} & {b} is {v}.")
elif a1 == "multiplication":
    i = multi(a,b)
    print(f"The multiplication of {a} & {b} is {i}.")
elif a1 == "division":
    n = divid(a,b)
    print(f"The Division of {a} & {b} is {n}.")
elif a1 == "average":
    t = avg(a,b)
    print(f"The Average of {a} & {b} is {t}.")
else:
    print("Wrong input, Please try again with correct mathematical operation as given below. Thank you!\n\
           1. addition\n\
           2. substraction\n\
           3. multiplication\n\
           4. division\n\
           5. average\n\
          ")

    


