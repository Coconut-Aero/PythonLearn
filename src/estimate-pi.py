import math


def pi(i):
    result = 0
    for j in range(1, i+1):
        result += math.pow(-1, j + 1) / (2.0 * j - 1)
    result *= 4
    return result


print("i    m(i)")
for i in range(100000):
    print(i, "    ", pi(i))
