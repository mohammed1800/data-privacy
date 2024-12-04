import hashlib

def hash_password_sha256(password):
    """
    Hashes a password using the SHA-256 algorithm.
    
    Parameters:
    password (str): The input password to be hashed.

    Returns:
    str: The SHA-256 hashed representation as a hexadecimal string.
    """
    # Encode the password to a bytes object
    encoded_password = password.encode('utf-8')
    
    # Create a SHA-256 hash object
    hash_object = hashlib.sha256()
    
    # Update the hash object with the encoded password
    hash_object.update(encoded_password)
    
    # Return the hexadecimal representation of the hash
    return hash_object.hexdigest()

# Example usage
if __name__ == "__main__":
    # Input password
    password = input("Enter your password: ")
    
    # Compute its SHA-256 hash
    hashed_password = hash_password_sha256(password)
    
    print("SHA-256 Hashed Password:")
    print(hashed_password)
