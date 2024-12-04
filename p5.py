import random

def load_words_from_file(file_path):
    """
    Loads words from a dictionary file into a list.
    
    Parameters:
    file_path (str): Path to the dictionary file.

    Returns:
    list: List of words from the file.
    """
    try:
        with open(file_path, 'r') as file:
            # Read lines, strip whitespace, and return as a list
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}.")
        return []

def generate_password(word_list, num_words=4, separator="-"):
    """
    Generates a password using random words from a word list.
    
    Parameters:
    word_list (list): List of words to choose from.
    num_words (int): Number of words in the password. Default is 4.
    separator (str): Separator between words in the password. Default is "-".

    Returns:
    str: Generated password.
    """
    if len(word_list) < num_words:
        print("Error: Not enough words in the word list to generate a password.")
        return ""

    # Randomly select words from the list
    selected_words = random.sample(word_list, num_words)
    
    # Join selected words with the separator
    return separator.join(selected_words)

# Example usage
if __name__ == "__main__":
    # Path to a dictionary file
    dictionary_file = "/usr/share/dict/words"  # Adjust path for your system or provide a custom file
    words = load_words_from_file(dictionary_file)

    if words:
        # Generate a password with 4 random words and '-' as a separator
        password = generate_password(words, num_words=4, separator="-")
        print("Generated Password:", password)
