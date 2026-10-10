"""
COVER
==================================================
Name: Jose Lizandro Villarreal Martínez
Student ID (Matrícula): 2630116
Group: IM 1-2
GitHub Repository: https://github.com/joselizandroupv/Tareas_Python
==================================================

EXECUTIVE SUMMARY
==================================================
In this assignment, we explore string manipulation and input validation in Python.
Strings are immutable sequences of text, meaning their values cannot be changed directly
after creation. Using standard methods such as strip(), split(), join(),
and string slicing, we clean, validate, and reformat user inputs across six practical
programming problems to prevent system errors.
==================================================

PRINCIPLES AND BEST PRACTICES
==================================================
- Strings are immutable: any modification creates a new string.
- It is best practice to normalize input with strip() and lower() before comparing.
- Avoid "magic numbers" in indexes; document what each slice extracts.
- Use native string methods instead of rewriting basic logic.
- Design clear validations: first check that it is not empty, then validate format.
- Write readable code: use lower_snake_case and descriptive error messages.
"""
# ==================================================
# Problem 1: Full name formatter
# Description: Reads a full name, normalizes it (removes extra spaces),
# formats it to Title Case, and extracts the initials.
#
# Inputs:
# - full_name (string)
#
# Outputs:
# - "Formatted name: <Name In Title Case>"
# - "Initials: <X.X.X.>"
#
# Validations:
# - Cannot be empty or only spaces.
# - Must contain at least two words.
#
# Test cases:
# 1) Normal: "  juan carlos tovar  "
# 2) Border: "luis      miguel" (extra spaces inside)
# 3) Error: "Ana" (only one word) or "   " (empty)
# ==================================================

print("--- Problem 1: Full Name Formatter ---")
full_name = input("Enter your full name: ")

# Remove leading and trailing spaces
cleaned_name = full_name.strip()

# Split the name into a list of words to count them
words = cleaned_name.split()

# Validation: Ensure it is not empty and has at least two words
if len(words) < 2:
    print("Error: invalid input. Please enter at least a first and last name.")
else:
    # Rejoin the words with a single space and apply Title Case
    formatted_name = " ".join(words).title()

    # Extract the first letter of each word for the initials
    initials = ""
    for word in words:
        initials += word[0].upper() + "."

    print(f"Formatted name: {formatted_name}")
    print(f"Initials: {initials}")
print("\n")

# ==================================================
# Problem 2: Simple email validator
# Description: Validates if an email contains exactly one '@',
# at least one '.' after the '@', and no spaces inside.
# Extracts the domain if valid.
#
# Inputs:
# - email_text (string)
#
# Outputs:
# - "Valid email: true" / "false"
# - "Domain: <domain_part>"
#
# Validations:
# - Not empty after strip().
# - Exactly one '@'.
# - No spaces inside the email.
# - At least one '.' after the '@'.
#
# Test cases:
# 1) Normal: "alumno@upv.edu.mx"
# 2) Border: "  correo@dominio.com  " (extra spaces around)
# 3) Error: "correo sin arroba" or "correo@dominio" (no dot)
# ==================================================

print("--- Problem 2: Simple Email Validator ---")
email_text = input("Enter your email: ")

# Remove accidental leading and trailing spaces
cleaned_email = email_text.strip()

# Variables to store the result
is_valid = False
domain = ""

# 1. Not empty and no spaces inside
if len(cleaned_email) > 0 and " " not in cleaned_email:
    # 2. Exactly one '@' symbol
    if cleaned_email.count("@") == 1:
        # Find the position (index) of the '@'
        at_index = cleaned_email.find("@")

    # Slice the text to get everything after the '@'
    domain_part = cleaned_email[at_index + 1 :]

    # 3. Verify there is at least one dot in the domain part
    if "." in domain_part:
        is_valid = True
        domain = domain_part

# Display the results according to the requirements
if is_valid:
    print("Valid email: true")
    print(f"Domain: {domain}")
else:
    print("Valid email: false")
print("\n")

# ==================================================
# Problem 3: Palindrome checker
# Description: Determines if a phrase is a palindrome by
# reading it backwards, ignoring spaces and letter case.
#
# Inputs:
# - phrase (string)
#
# Outputs:
# - "Normalized phrase: <...>"
# - "Is palindrome: true" / "false"
#
# Validations:
# - Not empty after strip().
# - Minimum length of 3 characters (excluding spaces).
#
# Test cases:
# 1) Normal: "Anita lava la tina"
# 2) Border: "  Ana  " (exact minimum length, trailing spaces)
# 3) Error: "  " (empty) or "No" (fails minimum length)
# ==================================================

print("--- Problem 3: Palindrome Checker ---")
phrase = input("Enter a phrase: ")

# Remove leading and trailing spaces
cleaned_phrase = phrase.strip()

# Normalize text: convert to lowercase and remove all internal spaces
normalized_phrase = cleaned_phrase.lower().replace(" ", "")

# Validation: Must not be empty and must have at least 3 valid characters
if len(normalized_phrase) == 0:
    print("Error: invalid input. The phrase cannot be empty.")
elif len(normalized_phrase) < 3:
    print("Error: phrase is too short. It must have at least 3 characters.")
else:
    # Slicing [::-1] reverses the string. We compare it to the original.
    is_palindrome = normalized_phrase == normalized_phrase[::-1]

    print(f"Normalized phrase: {normalized_phrase}")
    if is_palindrome:
        print("Is palindrome: true")
    else:
        print("Is palindrome: false")
print("\n")

# ==================================================
# Problem 4: Sentence word stats
# Description: Normalizes a sentence, splits it into words, and
# calculates total count, first, last, shortest, and longest words.
#
# Inputs:
# - sentence (string)
#
# Outputs:
# - "Word count: <n>"
# - "First word: <...>"
# - "Last word: <...>"
# - "Shortest word: <...>"
# - "Longest word: <...>"
#
# Validations:
# - Sentence not empty after strip().
# - Must contain at least one valid word.
#
# Test cases:
# 1) Normal: "The quick brown fox jumps"
# 2) Border: "  Hello  " (single word, extra spaces)
# 3) Error: "   " (empty after strip)
# ==================================================

print("--- Problem 4: Sentence Word Stats ---")
sentence = input("Enter a sentence: ")

# Normalize spaces
cleaned_sentence = sentence.strip()

# Validation: Ensure the string is not empty
if len(cleaned_sentence) == 0:
    print("Error: invalid input. Sentence cannot be empty.")
else:
    # Separate the text into a list of words
    words = cleaned_sentence.split()

    # Basic list indexing
    word_count = len(words)
    first_word = words[0]
    last_word = words[-1]  # Negative index gets the last item

    # Initialize variables for loop comparison
    shortest_word = words[0]
    longest_word = words[0]

    # Loop to find min and max length words
    for word in words:
        if len(word) < len(shortest_word):
            shortest_word = word
        if len(word) > len(longest_word):
            longest_word = word

    # Display results
    print(f"Word count: {word_count}")
    print(f"First word: {first_word}")
    print(f"Last word: {last_word}")
    print(f"Shortest word: {shortest_word}")
    print(f"Longest word: {longest_word}")
print("\n")

# ==================================================
# Problem 5: Password strength classifier
# Description: Evaluates a password and classifies it as
# weak, medium, or strong based on length and character types.
#
# Inputs:
# - password_input (string)
#
# Outputs:
# - "Password strength: weak"
# - "Password strength: medium"
# - "Password strength: strong"
#
# Validations:
# - Cannot be empty.
#
# Test cases:
# 1) Normal (Strong): "SuperP@ssw0rd!"
# 2) Border (Medium): "Password123" (Length >= 8, no symbol)
# 3) Error (Weak/Empty): "abc" (Too short) or "" (Empty)
# ==================================================

print("--- Problem 5: Password Strength Classifier ---")
password_input = input("Enter your password: ")

# Validation: Ensure it is not empty
if len(password_input) == 0:
    print("Error: invalid input. Password cannot be empty.")
else:
    # Boolean flags to track what we find
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    # Loop character by character
    for char in password_input:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_symbol = True

    pass_length = len(password_input)

    # Classification logic based on requirements
    if pass_length >= 8 and has_upper and has_lower and has_digit and has_symbol:
        print("Password strength: strong")
    elif pass_length >= 8 and (has_upper or has_lower) and (has_digit or has_symbol):
        print("Password strength: medium")
    else:
        print("Password strength: weak")
print("\n")

# ==================================================
# Problem 6: Product label formatter
# Description: Generates a fixed-width (30 characters) label
# combining product name and price. Pads with spaces or truncates.
#
# Inputs:
# - product_name (string)
# - price_value (string)
#
# Outputs:
# - "Label: '<exactly 30 characters>'"
#
# Validations:
# - product_name cannot be empty after strip().
# - price_value must be a valid positive number.
#
# Test cases:
# 1) Normal: "Coffee", "45.50" (Padded with spaces)
# 2) Border: "Super Ultra Mega Awesome Laptop", "999.99" (Truncated to 30)
# 3) Error: "   " (Empty product) or "abc" (Invalid price)
# ==================================================

print("--- Problem 6: Product Label Formatter ---")
product_name = input("Enter product name: ")
price_value = input("Enter product price (e.g. 45.50): ")

cleaned_name = product_name.strip()
cleaned_price = price_value.strip()

# Validation: Name not empty, price must be numbers (removing one dot to check if float)
is_valid_price = cleaned_price.replace(".", "", 1).isdigit()

if len(cleaned_name) == 0:
    print("Error: invalid input. Product name cannot be empty.")
elif not is_valid_price:
    print("Error: invalid input. Price must be a valid number.")
else:
    # Create the base label using f-strings
    base_label = f"Product: {cleaned_name} | Price: ${cleaned_price}"

    # Truncate if longer than 30 characters using slicing
    if len(base_label) > 30:
        final_label = base_label[:30]
    # Pad with spaces if shorter than 30 characters
    else:
        # ljust(30) automatically adds spaces to the right until it hits 30 characters
        final_label = base_label.ljust(30)

    print(f"Label: '{final_label}'")
print("\n")

"""

CONCLUSIONS
==================================================
Working with strings in Python taught me how important input validation is
before processing user data. Built-in functions like strip() and split() make 
text cleaning fast and easy, while slicing provides a quick way to extract or 
reverse content. Understanding string immutability helped me write cleaner code 
without modifying original variables accidentally.

REFERENCES
==================================================
1) Python Software Foundation. (n.d.). Built-in Types: Text Sequence Type — str. 
https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

2) Sweigart, A. (2019). Automate the Boring Stuff with Python. No Starch Press.

3) Python String Methods Tutorial. (n.d.). W3Schools. 
https://www.w3schools.com/python/python_ref_string.asp

4) Matthes, E. (2019). Python Crash Course. No Starch Press.

5) Real Python. (n.d.). Python String Formatting Best Practices. 
https://realpython.com/python-string-formatting/
"""
