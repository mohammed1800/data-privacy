import itertools
import string

def brute_force_attack(target_password, max_length=4):
    """
    Simulates a brute-force attack to guess a target password.
    
    Parameters:
    target_password (str): The password to guess.
    max_length (int): Maximum length of the password to attempt.

    Returns:
    str: The guessed password if found.
    int: Total number of attempts.
    """
    # Define the character set (adjust as needed)
    character_set = string.ascii_letters + string.digits + string.punctuation
    attempts = 0  # Counter for the number of attempts

    print("Starting brute-force attack...")
    # Iterate over all possible lengths up to max_length
    for length in range(1, max_length + 1):
        # Generate all possible combinations of the given length
        for guess in itertools.product(character_set, repeat=length):
            attempts += 1
            # Convert the tuple to a string
            guess_password = ''.join(guess)
            # Check if the guessed password matches the target
            if guess_password == target_password:
                return guess_password, attempts

    return None, attempts  # Return None if the password is not found

# Example usage
if __name__ == "__main__":
    target = input("Enter the password to brute-force: ")
    max_len = int(input("Enter the maximum length to try: "))

    guessed_password, total_attempts = brute_force_attack(target, max_len)
    
    if guessed_password:
        print(f"Password guessed successfully: '{guessed_password}'")
        print(f"Total attempts: {total_attempts}")
    else:
        print("Failed to guess the password within the given length.")
