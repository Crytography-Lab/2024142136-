text = input("Enter text: ")
key = input("Enter key: ")
l = []
n = len(key)
for i in range(n):
    l.append(i)
for i in range(n):
    for j in range(i + 1, n):
        if key[l[i]] > key[l[j]]:
            l[i], l[j] = l[j], l[i]
ct = ""
for k in l:
    for i in range(k, len(text), n):
        ct += text[i]
text = ct
ct = ""
for k in l:
    for i in range(k, len(text), n):
        ct += text[i]

print("Result:", ct)
