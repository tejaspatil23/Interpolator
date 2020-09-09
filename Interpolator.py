
x1 = float(input("Enter the first set of knowns: x = "))
y1 = float(input("Enter the first set of knowns: y = "))
x2 = float(input("Enter the second set of knowns: x = "))
y2 = float(input("Enter the second set of knowns: y = "))

x = str(input("Enter the objective x value (Enter \"X\" if unknown): "))
y = str(input("Enter the objective y value (Enter \"Y\" if unknown): "))

if x == str("X"):
    value = float(x1+(float(y)-y1)*((x2-x1)/(y2-y1)))
    print("X = " + str(value))

elif y == str("Y"):
    value = float(y1 +(float(x)-x1)*((y2-y1)/(x2-x1)))
    print("Y = " + str(value))

else:
    print("Interpolation cannot be performed.")
