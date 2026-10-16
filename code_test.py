for i in range(10):
    print(f"{i}: Hello World!")

for i in range(1,9):
    for j in range(1,9):
        print(f"{i*j:>3}",end="")
    print()

n = 2
m = 2

while True:
    res = True
    if n == 2:
        print(n)
    else:
        while n > m:
            if n % m == 0:
                res = False
            m += 1
        if res:
            print(n)
    n += 1