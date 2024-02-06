## Caesar Cipher  Encryption & Decryption

def encrypt(msg , shift):             ## Encryption Function
    Encrypted_Msg = ""
    for i in msg:
        if i.isalpha():                                         # Checking if it's a char
            En_ascii_order = ord(i) + int(shift)                # Ascii Code of the shifted Character
            En_letter = chr(En_ascii_order)                     # Convert the Ascii to Character
            Encrypted_Msg += '{:}'.format(En_letter)            # Align to one String
        else :
            Encrypted_Msg += i
    return Encrypted_Msg


def decrypt (Encrypted_Msg , shift):   ## Decryption Function
    return encrypt(Encrypted_Msg,-shift)      # No Need to write the reverse Algorithm,Just use the negtive value of the shift


def main():
    print('Caesar Cipher Encryption & Decryption')
    message = input("Enter Your Message : ")                      # Message
    shift = int(input("Enter the Shift Value : "))                # Shift Value
    encrypted_msg = encrypt(message,shift)
    print('Encrypted Message : ', format(encrypted_msg))          # Enrypted Message
    decrypted_msg = decrypt(encrypted_msg,shift)
    print('Decrypted Message : ', format(decrypted_msg))          # Decrypted Message

# Wait for user input before closing
    input("Press Enter to exit...")
    
if __name__ == "__main__":
    main()
