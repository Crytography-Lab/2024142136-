text = str(input("Enter text: ")).upper()
key = str(input("Enter key: ")).upper()
choice = int(input("Enter 1 for Encryption or 2 for Decryption: "))
result = ""
for i in text:
    if i.isalpha():
        if choice == 1:
            result += key[ord(i) - 65]
        elif choice == 2:
            j = key.index(i)
            result += chr(j + 65)
        else:
            print("Invalid choice")
            break
    else:
        result += i
print("Result:", result)
