for i in range(10):
    print(f"{i}: Hello World!")

for i in range(1,9):
    for j in range(1,9):
        print(f"{i*j:>3}",end="")
    print()