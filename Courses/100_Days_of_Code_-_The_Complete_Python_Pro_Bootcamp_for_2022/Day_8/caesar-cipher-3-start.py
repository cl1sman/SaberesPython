from unittest import result


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().


def caesar(text, shift, direction):
    def operation(plain_text=text, shift_amount=shift):
        the_text = ""
        for letter in plain_text:
            position = alphabet.index(letter)

            if direction == "encode":
                new_position = position + shift_amount

            elif direction == "decode":
                new_position = position - shift_amount

            the_text += alphabet[new_position]

        if direction == "encode":
            print(f"The encoded text is {the_text}")

        elif direction == "decode":
            print(f"The decoded text is {the_text}")
    return operation(text, shift)


# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(text, shift, direction)
