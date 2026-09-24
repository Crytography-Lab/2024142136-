text = input("Enter text : ").upper()
key = input("Enter key : ").upper()
s = ""
for i in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
    if i not in s:
        s += i
matrix = []
for i in range(0, 25, 5):
    matrix.append(s[i:i+5])
result = ""
for i in range(0, len(text), 2):
    a = text[i]
    b = text[i+1]
    for j in range(5):
        for k in range(5):
            if matrix[j][k] == a:
                j1, k1 = j, k
            if matrix[j][k] == b:
                j2, k2 = j, k
    if j1 == j2:
        result += matrix[j1][(k1+1) % 5]
        result += matrix[j2][(k2+1) % 5]
    elif k1 == k2:
        result += matrix[(j1+1) % 5][k1]
        result += matrix[(j2+1) % 5][k2]
    else:
        result += matrix[j1][k2]
        result += matrix[j2][k1]
print("Result:", result)
