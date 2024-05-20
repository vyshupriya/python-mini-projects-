rows = 5

# Print first row
print("* " * rows)

# Print middle rows
for i in range(rows - 2):
    print("* " + "  " * (rows - 2) + "*")

# Print last row
if rows > 1:
    print("* " * rows)
