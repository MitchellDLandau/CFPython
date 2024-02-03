a = int(input("First number: "))
b = int(input("Second number: "))
m = input(" + for addition - for subtraction: ")

if m == "+":
    print(a + b)
elif m == "-":
    print(a - b)
else: 
    print("unknown operator")