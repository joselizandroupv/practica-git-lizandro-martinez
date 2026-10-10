# ==============================================================================
# STUDENT INFORMATION / PORTADA
# ==============================================================================
# Student Name: Jose Lizandro Villarreal Martinez
# Student ID (Matricula): 2630116
# Group: IM 1 - 2
# ==============================================================================

# ==============================================================================
# EXECUTIVE SUMMARY / RESUMEN EJECUTIVO
# ==============================================================================
# A string in Python is an immutable sequence of characters used to store textual data.
# Because strings are immutable, any modification operation returns a new string rather
# than modifying the original one in place. Basic operations include concatenation,
# calculating length, extracting substrings via slicing, searching patterns, and replacing text.
# Validating and normalizing input text—such as emails, names, and passwords—is critical
# to ensure data integrity, prevent runtime errors, and avoid security vulnerabilities.
# This document covers 6 distinct problems demonstrating input design, format validation,
# string methods, and test case evaluation with executed Python code.
# ==============================================================================

# ==============================================================================
# PRINCIPLES AND BEST PRACTICES / PRINCIPIOS Y BUENAS PRÁCTICAS
# ==============================================================================
# 1. Strings are immutable: any transformation produces a new string object.
# 2. Always normalize input with strip() and case methods (lower()/upper()) before comparing.
# 3. Avoid magic numbers in indexing; document the intent of explicit slices.
# 4. Rely on standard string methods (e.g., find(), split()) rather than re-implementing logic.
# 5. Design clear validation logic: check for non-empty input first, then validate structure.
# 6. Write readable code: use self-explanatory variable names and clear output messages.
# ==============================================================================


# ==============================================================================
# Problem 1: Full name formatter (name + initials)
# Description: Normalizes full name input, converts it to Title Case, and extracts
#              first-letter initials separated by dots.
# Inputs:
#   - full_name (string)
# Outputs:
#   - Formatted name: <Name In Title Case>
#   - Initials: <X.X.X.>
# Validations:
#   - String must not be empty after strip().
#   - Must contain at least two words (first name and last name).
# Test cases:
#   1) Normal: "juan carlos tovar" -> Formatted name: Juan Carlos Tovar | Initials: J.C.T.
#   2) Border: "  a   b  " -> Formatted name: A B | Initials: A.B.
#   3) Error: "  " or "juan" -> Error: invalid input
# ==============================================================================


def problem_1_name_formatter(full_name_input):
    cleaned_name = full_name_input.strip()
    if not cleaned_name:
        print("Error: invalid input")
        return

    words = cleaned_name.split()
    if len(words) < 2:
        print("Error: invalid input")
        return

    formatted_name = " ".join(words).title()
    initials = ".".join([w[0].upper() for w in words]) + "."

    print(f"Formatted name: {formatted_name}")
    print(f"Initials: {initials}")


# ==============================================================================
# Problem 2: Simple email validator (structure + domain)
# Description: Validates basic email formatting rules (no spaces, single '@', dot
#              in domain) and extracts the email domain.
# Inputs:
#   - email_text (string)
# Outputs:
#   - Valid email: true / false
#   - Domain: <domain_part> (if valid)
# Validations:
#   - String must not be empty after strip().
#   - Must contain exactly one '@'.
#   - Must contain at least one '.' after the '@'.
#   - Must not contain spaces.
# Test cases:
#   1) Normal: "user@example.com" -> Valid email: true, Domain: example.com
#   2) Border: "a@b.c" -> Valid email: true, Domain: b.c
#   3) Error: "invalid@email" or "a @b.com" -> Valid email: false
# ==============================================================================


def problem_2_email_validator(email_text_input):
    email_text = email_text_input.strip()

    if not email_text or " " in email_text or email_text.count("@") != 1:
        print("Valid email: false")
        return

    at_index = email_text.find("@")
    domain_part = email_text[at_index + 1 :]

    if (
        "." not in domain_part
        or domain_part.startswith(".")
        or domain_part.endswith(".")
    ):
        print("Valid email: false")
        return

    print("Valid email: true")
    print(f"Domain: {domain_part}")


# ==============================================================================
# Problem 3: Palindrome checker (ignoring spaces and case)
# Description: Determines whether a given phrase reads the same backward as forward,
#              ignoring whitespace and case differences.
# Inputs:
#   - phrase (string)
# Outputs:
#   - Is palindrome: true / false
# Validations:
#   - String must not be empty after strip().
#   - Cleaned string must have a minimum length of 3 characters.
# Test cases:
#   1) Normal: "Anita lava la tina" -> Is palindrome: true
#   2) Border: "A  b   a" -> Is palindrome: true
#   3) Error: "  " or "hi" -> Error: invalid input
# ==============================================================================


def problem_3_palindrome_checker(phrase_input):
    cleaned_phrase = phrase_input.strip()
    if not cleaned_phrase:
        print("Error: invalid input")
        return

    normalized_text = cleaned_phrase.lower().replace(" ", "")
    if len(normalized_text) < 3:
        print("Error: invalid input")
        return

    is_pal = normalized_text == normalized_text[::-1]
    print(f"Is palindrome: {'true' if is_pal else 'false'}")


# ==============================================================================
# Problem 4: Sentence word stats (lengths and first/last word)
# Description: Analyzes a sentence to calculate total word count, identifies first and
#              last words, and finds the shortest and longest words.
# Inputs:
#   - sentence (string)
# Outputs:
#   - Word count: <n>
#   - First word: <...>
#   - Last word: <...>
#   - Shortest word: <...>
#   - Longest word: <...>
# Validations:
#   - Sentence must not be empty after strip().
#   - Must contain at least one valid word after split().
# Test cases:
#   1) Normal: "Python is a powerful programming language" -> Stats printed.
#   2) Border: "  Hello  " -> Single word stats.
#   3) Error: "    " -> Error: invalid input
# ==============================================================================


def problem_4_word_stats(sentence_input):
    cleaned_sentence = sentence_input.strip()
    if not cleaned_sentence:
        print("Error: invalid input")
        return

    words = cleaned_sentence.split()
    if not words:
        print("Error: invalid input")
        return

    word_count = len(words)
    first_word = words[0]
    last_word = words[-1]

    shortest_word = min(words, key=len)
    longest_word = max(words, key=len)

    print(f"Word count: {word_count}")
    print(f"First word: {first_word}")
    print(f"Last word: {last_word}")
    print(f"Shortest word: {shortest_word}")
    print(f"Longest word: {longest_word}")


# ==============================================================================
# Problem 5: Password strength classifier
# Description: Classifies a password into 'weak', 'medium', or 'strong' based on
#              length, uppercase, lowercase, numeric, and special character presence.
# Inputs:
#   - password_input (string)
# Outputs:
#   - Password strength: weak / medium / strong
# Validations:
#   - Password must not be empty.
# Test cases:
#   1) Normal: "P@ssw0rd2026!" -> Password strength: strong
#   2) Border: "Pass1234" -> Password strength: medium
#   3) Error: "" or "12345" -> Password strength: weak
# ==============================================================================


def problem_5_password_classifier(password_input):
    if not password_input:
        print("Error: invalid input")
        return

    pass_len = len(password_input)
    has_upper = any(c.isupper() for c in password_input)
    has_lower = any(c.islower() for c in password_input)
    has_digit = any(c.isdigit() for c in password_input)
    has_symbol = any(not c.isalnum() for c in password_input)

    if pass_len >= 8 and has_upper and has_lower and has_digit and has_symbol:
        strength = "strong"
    elif pass_len >= 8 and ((has_upper and has_lower) or (has_lower and has_digit)):
        strength = "medium"
    else:
        strength = "weak"

    print(f"Password strength: {strength}")


# ==============================================================================
# Problem 6: Product label formatter (fixed-width text)
# Description: Generates a product label formatted as 'Product: <NAME> | Price: $<PRICE>'
#              ensuring the total string length is exactly 30 characters.
# Inputs:
#   - product_name (string)
#   - price_value (number or string)
# Outputs:
#   - Label: <exactly 30 characters>
# Validations:
#   - product_name must not be empty after strip().
#   - price_value must be convertible to a positive float.
# Test cases:
#   1) Normal: "Laptop", 999.99 -> Label padded to 30 chars.
#   2) Border: "Super Ultra High End Gaming Laptop", 2500 -> Label truncated to 30 chars.
#   3) Error: "", -50 -> Error: invalid input
# ==============================================================================


def problem_6_label_formatter(product_name_input, price_value_input):
    cleaned_name = str(product_name_input).strip()

    if not cleaned_name:
        print("Error: invalid input")
        return

    try:
        price_num = float(price_value_input)
        if price_num <= 0:
            print("Error: invalid input")
            return
    except ValueError:
        print("Error: invalid input")
        return

    base_label = f"Product: {cleaned_name} | Price: ${price_num:.2f}"

    if len(base_label) > 30:
        final_label = base_label[:30]
    else:
        final_label = base_label.ljust(30)

    print(f'Label: "{final_label}"')


# ==============================================================================
# EXECUTION OF TEST CASES
# ==============================================================================
if __name__ == "__main__":
    print("--- PROBLEM 1 TESTS ---")
    problem_1_name_formatter("juan carlos tovar")
    problem_1_name_formatter("  a   b  ")
    problem_1_name_formatter("   ")

    print("\n--- PROBLEM 2 TESTS ---")
    problem_2_email_validator("user@example.com")
    problem_2_email_validator("a@b.c")
    problem_2_email_validator("invalid@email")

    print("\n--- PROBLEM 3 TESTS ---")
    problem_3_palindrome_checker("Anita lava la tina")
    problem_3_palindrome_checker("A  b   a")
    problem_3_palindrome_checker("hi")

    print("\n--- PROBLEM 4 TESTS ---")
    problem_4_word_stats("Python is a powerful programming language")
    problem_4_word_stats("  Hello  ")
    problem_4_word_stats("    ")

    print("\n--- PROBLEM 5 TESTS ---")
    problem_5_password_classifier("P@ssw0rd2026!")
    problem_5_password_classifier("Pass1234")
    problem_5_password_classifier("12345")

    print("\n--- PROBLEM 6 TESTS ---")
    problem_6_label_formatter("Laptop", 999.99)
    problem_6_label_formatter("Super Ultra High End Gaming Laptop", 2500)
    problem_6_label_formatter("", -50)


# ==============================================================================
# CONCLUSIONS / CONCLUSIONES
# ==============================================================================
# Working with strings is fundamental to almost every software application because
# text represents the primary interface for user input and data output.
# Methods such as lower(), strip(), split(), and join() allow developers to standardize
# raw text and prevent bugs caused by inconsistent casing or unintended spaces.
# Normalizing data prior to comparison ensures consistent logic evaluation across systems.
# Furthermore, proper input validation prevents malformed data from propagating
# through a program, avoiding runtime exceptions and unexpected system behavior.
# String immutability requires returning new strings for every transformation,
# encouraging clear assignment patterns and memory awareness when using slices.
# ==============================================================================

# ==============================================================================
# REFERENCES / REFERENCIAS
# ==============================================================================
# References:
# 1) Python Software Foundation. (2026). Text Sequence Type — str. Python Documentation.
#    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
# 2) Python Software Foundation. (2026). Common String Operations. Python Documentation.
#    https://docs.python.org/3/library/string.html
# 3) Sweigart, A. (2020). Automate the Boring Stuff with Python: Practical Programming for Total Beginners. No Starch Press.
# 4) Lutz, M. (2013). Learning Python: Powerful Object-Oriented Programming. O'Reilly Media.
# 5) Real Python. (2026). Python String Formatting Best Practices.
#    https://realpython.com/python-string-formatting/
# ==============================================================================
