text = input("Enter text: ")
depth = int(input("Enter depth: "))
rail = []
for i in range(depth):
    rail.append([])
row = 0
direction = 1
for i in range(len(text)):
    rail[row].append(i)
    if row == 0:
        direction = 1
    elif row == depth - 1:
        direction = -1
    row += direction
for i in range(depth):
    print(i, rail[i])
ct = ""
for i in range(depth):
    for j in rail[i]:
        ct += text[j]

print("Result:", ct)
