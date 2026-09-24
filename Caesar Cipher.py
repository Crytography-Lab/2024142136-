text = str(input("Enter text: ")).upper()
key = int(input("Enter key: "))
choice = int(input("Enter 1 for Encryption or 2 for Decryption: "))
result = ""
for i in text:
    if i.isalpha():
        j = ord(i) - 65
        if choice == 1:
            result += chr((j + key) % 26 + 65)
        elif choice == 2:
            result += chr((j - key) % 26 + 65)
        else:
            print("Invalid choice")
            break
    else:
        result += i
print("Result:", result.lower())
