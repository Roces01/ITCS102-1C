y = eval(input("Input a number-->"))
X = 1
for y in range(y,0,-1):
    X *= y
    print("The Factorial of", y, "is",X)
