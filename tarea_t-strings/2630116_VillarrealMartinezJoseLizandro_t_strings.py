# STUDENT INFORMATION / PORTADA
"""
Student Name: Jose Lizandro Villarreal Martinez
Student ID (Matricula): 2630116
Group: IM 1 - 2
"""

# EXECUTIVE SUMMARY / RESUMEN EJECUTIVO
"""
A string in Python is an immutable sequence of characters used to store text.
Because strings are immutable, any modification creates a brand new string
instead of changing the original string in place. Basic string operations
include concatenation, calculating length, slicing substrings, searching,
and replacing text. Validating and normalizing input text—such as names, emails,
and passwords—is essential to prevent program crashes, clean formatting errors,
and maintain data integrity. This script covers 6 distinct problems showcasing
input design, string methods, format validations, and test case execution.
"""


# PRINCIPLES AND BEST PRACTICES / PRINCIPIOS Y BUENAS PRÁCTICAS
"""
1. Strings are immutable, transformations always return a new string object.

2. Normalize input with strip() and lower()/upper() before running comparisons.

3. Avoid magic numbers in indexing and document explicit slice behavior.

4. Use built-in string methods (e.g., find(), split()) instead of custom logic.

5. Build clear validation flows: verify non-empty input first, then structure.

6. Write clean code using self-explanatory lower_snake_case variable names.
"""


# PROBLEM 1: FULL NAME FORMATTER (NAME + INITIALS)
"""
Description: 
Normalizes full name input, converts it to Title Case, and extracts
first-letter initials separated by dots.

Inputs:
- full_name_input (string)

Outputs:
- Formatted name: <Name In Title Case>
- Initials: <X.X.X.>

Validations:
- String must not be empty after strip().
- Must contain at least two words (first name and last name).

Test cases:
1) Normal: "juan carlos tovar" -> Formatted name: Juan Carlos Tovar | Initials: J.C.T.
2) Border: "  a   b  " -> Formatted name: A B | Initials: A.B.
3) Error: "  " or "juan" -> Error: invalid input
"""

print("--- PROBLEM 1 TESTS ---")

p1_test_inputs = ["juan carlos tovar", "  a   b  ", "   "]

for full_name_input in p1_test_inputs:
    cleaned_name = full_name_input.strip()

    if not cleaned_name:
        print("Error: invalid input")
    else:
        words = cleaned_name.split()

        if len(words) < 2:
            print("Error: invalid input")
        else:
            formatted_name = " ".join(words).title()

            initials_list = []
            for word in words:
                initials_list.append(word[0].upper())

            initials = ".".join(initials_list) + "."

            print(f"Formatted name: {formatted_name}")
            print(f"Initials: {initials}")


# PROBLEM 2: SIMPLE EMAIL VALIDATOR (STRUCTURE + DOMAIN)
"""
Description: 
Validates basic email formatting rules (no spaces, single '@', dot
in domain) and extracts the email domain.

Inputs:
- email_text_input (string)

Outputs:
- Valid email: true / false
- Domain: <domain_part> (if valid)

Validations:
- String must not be empty after strip().
- Must contain exactly one '@'.
- Must contain at least one '.' after the '@'.
- Must not contain spaces.

Test cases:
1) Normal: "user@example.com" -> Valid email: true, Domain: example.com
2) Border: "a@b.c" -> Valid email: true, Domain: b.c
3) Error: "invalid@email" or "a @b.com" -> Valid email: false
"""

print("\n--- PROBLEM 2 TESTS ---")

p2_test_inputs = ["user@example.com", "a@b.c", "invalid@email"]

for email_text_input in p2_test_inputs:
    cleaned_email = email_text_input.strip()

    if not cleaned_email or " " in cleaned_email or cleaned_email.count("@") != 1:
        print("Valid email: false")
    else:
        at_index = cleaned_email.find("@")
        domain_part = cleaned_email[at_index + 1 :]

        if (
            "." not in domain_part
            or domain_part.startswith(".")
            or domain_part.endswith(".")
        ):
            print("Valid email: false")
        else:
            print("Valid email: true")
            print(f"Domain: {domain_part}")


# PROBLEM 3: PALINDROME CHECKER (IGNORING SPACES AND CASE)
"""
Description: 
Determines whether a given phrase reads the same backward as forward,
ignoring whitespace and case differences.

Inputs:
- phrase_input (string)

Outputs:
- Is palindrome: true / false

Validations:
- String must not be empty after strip().
- Cleaned string must have a minimum length of 3 characters.

Test cases:
1) Normal: "Anita lava la tina" -> Is palindrome: true
2) Border: "A  b   a" -> Is palindrome: true
3) Error: "  " or "hi" -> Error: invalid input
"""

print("\n--- PROBLEM 3 TESTS ---")

p3_test_inputs = ["Anita lava la tina", "A  b   a", "hi"]

for phrase_input in p3_test_inputs:
    cleaned_phrase = phrase_input.strip()

    if not cleaned_phrase:
        print("Error: invalid input")
    else:
        normalized_text = cleaned_phrase.lower().replace(" ", "")

        if len(normalized_text) < 3:
            print("Error: invalid input")
        else:
            if normalized_text == normalized_text[::-1]:
                print("Is palindrome: true")
            else:
                print("Is palindrome: false")


# PROBLEM 4: SENTENCE WORD STATS (LENGTHS AND FIRST/LAST WORD)
"""
Description: 
Analyzes a sentence to calculate total word count, identifies first and
last words, and finds the shortest and longest words.

Inputs:
- sentence_input (string)

Outputs:
- Word count: <n>
- First word: <...>
- Last word: <...>
- Shortest word: <...>
- Longest word: <...>

Validations:
- Sentence must not be empty after strip().
- Must contain at least one valid word after split().

Test cases:
1) Normal: "Python is a powerful programming language" -> Stats printed.
2) Border: "  Hello  " -> Single word stats.
3) Error: "    " -> Error: invalid input
"""

print("\n--- PROBLEM 4 TESTS ---")

p4_test_inputs = [
    "Python is a powerful programming language",
    "  Hello  ",
    "    ",
]

for sentence_input in p4_test_inputs:
    cleaned_sentence = sentence_input.strip()

    if not cleaned_sentence:
        print("Error: invalid input")
    else:
        words = cleaned_sentence.split()

        if not words:
            print("Error: invalid input")
        else:
            word_count = len(words)
            first_word = words[0]
            last_word = words[-1]

            shortest_word = words[0]
            longest_word = words[0]

            for word in words:
                if len(word) < len(shortest_word):
                    shortest_word = word
                if len(word) > len(longest_word):
                    longest_word = word

            print(f"Word count: {word_count}")
            print(f"First word: {first_word}")
            print(f"Last word: {last_word}")
            print(f"Shortest word: {shortest_word}")
            print(f"Longest word: {longest_word}")


# PROBLEM 5: PASSWORD STRENGTH CLASSIFIER
"""
Description: 
Classifies a password into 'weak', 'medium', or 'strong' based on
length, uppercase, lowercase, numeric, and special character presence.

Inputs:
- password_input (string)

Outputs:
- Password strength: weak / medium / strong

Validations:
- Password must not be empty.

Test cases:
1) Normal: "P@ssw0rd2026!" -> Password strength: strong
2) Border: "Pass1234" -> Password strength: medium
3) Error: "" or "12345" -> Password strength: weak
"""

print("\n--- PROBLEM 5 TESTS ---")

p5_test_inputs = ["P@ssw0rd2026!", "Pass1234", "12345"]

for password_input in p5_test_inputs:
    if not password_input:
        print("Error: invalid input")
    else:
        pass_len = len(password_input)
        has_upper = False
        has_lower = False
        has_digit = False
        has_symbol = False

        for char in password_input:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True
            elif not char.isalnum():
                has_symbol = True

        if pass_len >= 8 and has_upper and has_lower and has_digit and has_symbol:
            strength = "strong"
        elif pass_len >= 8 and ((has_upper and has_lower) or (has_lower and has_digit)):
            strength = "medium"
        else:
            strength = "weak"

        print(f"Password strength: {strength}")


# PROBLEM 6: PRODUCT LABEL FORMATTER (FIXED-WIDTH TEXT)

"""
Description: 
Generates a product label formatted as 'Product: <NAME> | Price: $<PRICE>'
ensuring the total string length is exactly 30 characters.

Inputs:
- product_name_input (string)
- price_value_input (number or string)

Outputs:
- Label: <exactly 30 characters>

Validations:
- product_name_input must not be empty after strip().
- price_value_input must be convertible to a positive float.

Test cases:
1) Normal: "Laptop", 999.99 -> Label padded to 30 chars.
2) Border: "Super Ultra High End Gaming Laptop", 2500 -> Label truncated to 30 chars.
3) Error: "", -50 -> Error: invalid input
"""

print("\n--- PROBLEM 6 TESTS ---")

p6_test_cases = [
    ("Laptop", 999.99),
    ("Super Ultra High End Gaming Laptop", 2500),
    ("", -50),
]

for product_name_input, price_value_input in p6_test_cases:
    cleaned_name = str(product_name_input).strip()

    if not cleaned_name:
        print("Error: invalid input")
    else:
        try:
            price_num = float(price_value_input)
            if price_num <= 0:
                print("Error: invalid input")
            else:
                base_label = f"Product: {cleaned_name} | Price: ${price_num:.2f}"

                if len(base_label) > 30:
                    final_label = base_label[:30]
                else:
                    missing_spaces = 30 - len(base_label)
                    final_label = base_label + (" " * missing_spaces)

                print(f'Label: "{final_label}"')
        except ValueError:
            print("Error: invalid input")


# CONCLUSIONS / CONCLUSIONES
"""
String manipulation is fundamental in software development as text forms the main
communication channel between users and programs.

Methods such as lower(), strip(), split(), and join() allow developers to standardize
user inputs and clean unexpected whitespace or irregular capitalization.

Normalizing data prior to evaluation prevents logical errors and security flaws.
In addition, strict input validation prevents program execution errors.

String immutability requires storing transformed strings in new variables,
promoting clear assignment patterns and effective memory management.
"""


# REFERENCES / REFERENCIAS
"""
1) Python Software Foundation. (2026). Text Sequence Type — str. Python Documentation.
   https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

2) Python Software Foundation. (2026). Common String Operations. Python Documentation.
   https://docs.python.org/3/library/string.html

3) Sweigart, A. (2020). Automate the Boring Stuff with Python: Practical Programming for Total Beginners. No Starch Press.

4) Lutz, M. (2013). Learning Python: Powerful Object-Oriented Programming. O'Reilly Media.

5) Real Python. (2026). Python String Formatting Best Practices.
   https://realpython.com/python-string-formatting/
"""
