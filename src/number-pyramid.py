import math

for i in range(1, 8):
    for j in range(1, (20 - i) + 1):
        print("    ", end="")
    for j in range(0, i):
        print("{:^4d} ".format(int(math.pow(2, j))), end="")
    for j in range(i-2, -1, -1):
        print("{:^4d} ".format(int(math.pow(2, j))), end="")
    print()
