text = str(input("Enter text: ")).upper()
key = str(input("Enter key: ")).upper()
choice = int(input("Enter 1 for Encryption or 2 for Decryption: "))
result = ""
j = 0
for i in text:
    if i.isalpha():
        p = ord(i) - 65
        k = ord(key[j % len(key)]) - 65
        if choice == 1:
            result += chr((p + k) % 26 + 65)
        elif choice == 2:
            result += chr((p - k) % 26 + 65)
        else:
            print("Invalid choice")
            break
        j += 1
    else:
        result += i
print("Result:", result)
