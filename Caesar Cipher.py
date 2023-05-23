alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']







def caesar(text, shift, direction):
    encrypt_text =""
    if shift >26:
        shift = shift % 26
    for i in text:
        if i in alphabet:
            index =  alphabet.index(i)
            if direction == "encode":
                encrypt_text += alphabet[index+shift]
            elif direction == "decode":
                encrypt_text += alphabet[index-shift]
        else:
            encrypt_text +=i
    print(f"The {direction} text is {encrypt_text}")




loop = True
while loop == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: or exit \n").lower()
    
    if direction =="exit":
        print("Have a nice day! ")
        loop = False
    elif direction == "encode" or direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(text, shift, direction)
    
    again = input("want to restart the cipher program? Type 'yes' or 'No' \n").lower()
    if again == "no":
        loop = False
        print("Have a nice day! ")


   


