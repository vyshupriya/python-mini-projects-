rows = 5
start_num = 1
step = 2

for i in range(1, rows + 1):
    num = start_num
    for j in range(1, i + 1):
        print(num, end=" ")
        num += step
    print()
