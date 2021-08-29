XY = input()
X = XY.split(".")[0]
Y = int(XY.split(".")[1])

if 0 <= Y <= 2:
    print(X + "-")

elif 3 <= Y <= 6:
    print(X)

else:
    print(X + "+")
