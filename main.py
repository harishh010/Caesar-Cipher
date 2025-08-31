import art
from words import alphabets   # alphabets should be a list of letters a-z

print(art.logo)

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    # Reverse shift for decoding
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabets:   # Keep symbols/spaces unchanged
            output_text += letter
        else:
            shifted_position = (alphabets.index(letter) + shift_amount) % len(alphabets)
            output_text += alphabets[shifted_position]

    print(f"\nHere is the {encode_or_decode}d result: {output_text}\n")


def main():
    should_continue = True
    while should_continue:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        # Normalize shift to avoid unnecessary large numbers
        shift = shift % len(alphabets)

        caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

        restart = input("Type 'yes' to go again, otherwise type 'no':\n").lower()
        if restart == "no":
            should_continue = False
            print("GOODBYE 👋")


if __name__ == "__main__":
    main()
