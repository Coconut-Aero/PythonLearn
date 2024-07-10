def arrayprint(a):
    for i in a:
        print(i, end=" ")

a = []
for i in range(10):
    num = int(input("Enter a number: "))
    a.append(num)

arrayprint(a)