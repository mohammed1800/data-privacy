def encrypt(plaintext, shift): 

    encrypted_text = "" 

     

    for char in plaintext: 

        if char.isalpha():   

             

            shift_base = 65 if char.isupper() else 97 

            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base) 

            encrypted_text += encrypted_char 

        else: 

            encrypted_text += char   

     

    return encrypted_text 

 

 

def decrypt(ciphertext, shift): 

    decrypted_text = "" 

     

    for char in ciphertext: 

        if char.isalpha():  # Check if the character is a letter 

             

            shift_base = 65 if char.isupper() else 97 

            decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base) 

            decrypted_text += decrypted_char 

        else: 

            decrypted_text += char  # Non-alphabetic characters remain unchanged 

     

    return decrypted_text 

 

 

def main(): 

    plaintext = input("Enter the text to encrypt: ") 

    shift = int(input("Enter the shift value: ")) 

 

     

    encrypted_text = encrypt(plaintext, shift) 

    print(f"Encrypted text: {encrypted_text}") 

 

     

    decrypted_text = decrypt(encrypted_text, shift) 

    print(f"Decrypted text: {decrypted_text}") 

 

if __name__ == "__main__": 

    main() 