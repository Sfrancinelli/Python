alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text,shift,direction):
    cipher_text = ""
    decoded_text = ""
    for char in text:
        for i in alphabet:
            if char == i:
                index = alphabet.index(char)
                if direction == "encode":
                    index += shift
                    if index >= len(alphabet):
                        rest = index - len(alphabet)
                        index = rest
                    coded = alphabet[index]
                    cipher_text += coded
                elif direction == "decode":
                    index -= shift
                    if index < 0:
                        rest = len(alphabet) + index 
                        index = rest
                    decoded = alphabet[index]
                    decoded_text += decoded
    if direction == "encode":
        print(f"The encoded text is {cipher_text} and the shift number is {shift}")
    elif direction == "decode":
        print(f"The decoded text is {decoded_text} and the shift number is {shift}")

if direction == "encode" or direction == "decode":
    caesar(text,shift,direction)