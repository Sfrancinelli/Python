alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# 25 index
# civilization = hnAnqnEfynts
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text,shift):
    cipher_text = ""
    for char in text:
        for i in alphabet:
            if char == i:
                index = alphabet.index(char)
                print(f"normal index is {index}")
                index += shift
                print(f"shifted index is {index}")
                if index >= len(alphabet):
                    rest = index - len(alphabet)
                    index = rest
                    print(f"new index is {index}")
                coded = alphabet[index]
                cipher_text += coded
    print(f"The encoded text is {cipher_text} and the shift number is {shift}")

if direction == "encode":
    encrypt(text,shift)