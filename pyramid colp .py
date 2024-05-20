rows = 5
for i in range(0, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for j in range(0, i + 1):
        print("*", end="")
    for j in range(0, i):
        print(i, end="")
    print()
