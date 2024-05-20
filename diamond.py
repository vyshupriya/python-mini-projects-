rows = 5

# Upper half of the rhombus
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    print("* " * i)

# Lower half of the rhombus
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i), end="")
    print("* " * i)
