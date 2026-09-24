#Encryption
import numpy as np
text = str(input("Enter text: ")).upper()
key = np.array([[3, 3],
                [2, 5]])
result = ""
for i in range(0, len(text), 2):
    p = np.array([ord(text[i]) - 65,
                  ord(text[i + 1]) - 65])
    c = np.dot(key, p) % 26
    result += chr(c[0] + 65)
    result += chr(c[1] + 65)

print("Result:", result)



#Decryption
import numpy as np
text = str(input("Enter text: ")).upper()
key = np.array([[3, 3],
                [2, 5]])
result = ""
for i in range(0, len(text), 2):
    p = np.array([ord(text[i]) - 65,
                  ord(text[i + 1]) - 65])
    c = np.dot(key, p) % 26
    result += chr(c[0] + 65)
    result += chr(c[1] + 65)

print("Result:", result)
