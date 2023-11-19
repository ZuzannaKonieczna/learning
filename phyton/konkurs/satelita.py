n, p, M = map(int, input().split())

# Initialize a and b as lists of lists
a = [[0] * n for _ in range(p)]
b = [[0] * n for _ in range(p)]

# Input values for a and b
for i in range(p):
    a[i], b[i] = map(int, input().split())

# Print the values for debugging
for i in range(p):
    print("a", i, "= ", a[i], "b1 ",i,"= ", b[i])