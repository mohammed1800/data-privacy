def rail_fence_encrypt(text, key):
    """
    Encrypts the given text using Rail Fence Cipher.
    
    Parameters:
    text (str): The plaintext to encrypt.
    key (int): Number of rails (rows) to use.

    Returns:
    str: Encrypted text (ciphertext).
    """
    # Create a 2D list to represent the zigzag pattern
    rail = [['' for _ in range(len(text))] for _ in range(key)]
    direction_down = False  # Flag to track direction
    row, col = 0, 0  # Start from the top rail

    # Place each character in the zigzag pattern
    for char in text:
        rail[row][col] = char
        col += 1

        # Change direction if we reach the top or bottom rail
        if row == 0 or row == key - 1:
            direction_down = not direction_down

        # Move to the next rail in the current direction
        row += 1 if direction_down else -1

    # Read the characters row by row to form the ciphertext
    encrypted_text = ''.join(''.join(rail[row]) for row in range(key))
    return encrypted_text


def rail_fence_decrypt(ciphertext, key):
    """
    Decrypts the given text using Rail Fence Cipher.

    Parameters:
    ciphertext (str): The ciphertext to decrypt.
    key (int): Number of rails (rows) to use.

    Returns:
    str: Decrypted text (plaintext).
    """
    # Create a 2D list to represent the zigzag pattern
    rail = [['' for _ in range(len(ciphertext))] for _ in range(key)]
    direction_down = False
    row, col = 0, 0

    # Mark the zigzag positions with placeholders
    for i in range(len(ciphertext)):
        rail[row][col] = '*'
        col += 1

        if row == 0 or row == key - 1:
            direction_down = not direction_down

        row += 1 if direction_down else -1

    # Fill the marked positions with the ciphertext characters
    index = 0
    for i in range(key):
        for j in range(len(ciphertext)):
            if rail[i][j] == '*' and index < len(ciphertext):
                rail[i][j] = ciphertext[index]
                index += 1

    # Read the zigzag pattern to reconstruct the plaintext
    decrypted_text = []
    row, col = 0, 0
    direction_down = False
    for i in range(len(ciphertext)):
        decrypted_text.append(rail[row][col])
        col += 1

        if row == 0 or row == key - 1:
            direction_down = not direction_down

        row += 1 if direction_down else -1

    return ''.join(decrypted_text)


# Example usage
if __name__ == "__main__":
    plaintext = "HELLOTRANSPOSITION"
    key = 3  # Number of rails
    print("Plaintext:", plaintext)
    
    # Encrypt the plaintext
    encrypted = rail_fence_encrypt(plaintext, key)
    print("Encrypted Text:", encrypted)
    
    # Decrypt the ciphertext
    decrypted = rail_fence_decrypt(encrypted, key)
    print("Decrypted Text:", decrypted)