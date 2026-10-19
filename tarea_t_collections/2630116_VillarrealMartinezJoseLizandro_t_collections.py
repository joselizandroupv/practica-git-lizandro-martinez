# STUDENT INFORMATION
"""
Student Name: Jose Lizandro Villarreal Martinez
Student ID (Matricula): 2630116
Group: IM 1 - 2
"""

# EXECUTIVE SUMMARY
"""
In Python, lists (list) and tuples (tuple) are fundamental sequence collections used to
store and organize multiple data items. A list is an ordered, mutable collection that
allows adding, removing, and updating elements dynamically. A tuple is an ordered,
immutable collection designed for fixed data sequences that should not change during execution.
Understanding the distinction between mutability and immutability ensures efficient memory
usage and data integrity. This document covers two practical programming problems demonstrating
list manipulation (parsing, appending, counting, searching) and tuple representation for
2D spatial coordinates (calculating Euclidean distance and midpoint values).
"""


# PRINCIPLES AND BEST PRACTICES
"""
1. Choose lists for dynamic data where elements are added, removed, or modified frequently.

2. Choose tuples for fixed records, such as spatial coordinates, that must remain immutable.

3. Always validate sequence inputs to prevent processing empty strings or invalid data types.

4. Use clear lower_snake_case variable names to maintain clean and readable academic code.

5. Print boolean outputs formatted in lowercase (true or false) to follow output requirements.
"""


# PROBLEM 1: SHOPPING LIST BASICS (LIST OPERATIONS)
"""
Description: 
Manages a shopping list by parsing initial items from a string, appending a new
product to the list, computing the total item count, and verifying if a search item exists.

Inputs:
- initial_items_text (string)
- new_item (string)
- search_item (string)

Outputs:
- Items list: <items_list>
- Total items: <len_list>
- Found item: true / false

Validations:
- Inputs must not be empty after strip().
- Split initial items by comma and clean whitespace.

Test cases:
1) Normal: "apple,banana,orange", "grape", "banana" -> Found item: true
2) Border: "apple", "pear", "apple" -> Found item: true
3) Error: "", "grape", "banana" -> Error: invalid input
"""

print("--- PROBLEM 1 TESTS ---")

p1_test_cases = [
    ("apple,banana,orange", "grape", "banana"),
    ("apple", "pear", "apple"),
    ("", "grape", "banana"),
]

for initial_items_text, new_item, search_item in p1_test_cases:
    init_txt = str(initial_items_text).strip()
    n_item = str(new_item).strip()
    s_item = str(search_item).strip()

    if not init_txt or not n_item or not s_item:
        print("Error: invalid input")
    else:
        raw_items = init_txt.split(",")
        items_list = []

        for item in raw_items:
            cleaned = item.strip()
            if cleaned:
                items_list.append(cleaned)

        items_list.append(n_item)
        total_items = len(items_list)
        is_found = s_item in items_list

        print(f"Items list: {items_list}")
        print(f"Total items: {total_items}")
        print(f"Found item: {str(is_found).lower()}")


# PROBLEM 2: POINTS AND DISTANCES WITH TUPLES
"""
Description: 
Uses tuples to represent 2D points (x1, y1) and (x2, y2), calculating the
Euclidean distance and the midpoint tuple between them.

Inputs:
- x1, y1, x2, y2 (float)

Outputs:
- Point A: (x1, y1)
- Point B: (x2, y2)
- Distance: <distance>
- Midpoint: (mx, my)

Validations:
- Verify that all four coordinate inputs are valid numerical values (int or float).

Test cases:
1) Normal: 0.0, 0.0, 3.0, 4.0 -> Distance: 5.0, Midpoint: (1.5, 2.0)
2) Border: 2.0, 2.0, 2.0, 2.0 -> Distance: 0.0, Midpoint: (2.0, 2.0)
3) Error: "abc", 0.0, 3.0, 4.0 -> Error: invalid input
"""

print("\n--- PROBLEM 2 TESTS ---")

p2_test_cases = [
    (0.0, 0.0, 3.0, 4.0),
    (2.0, 2.0, 2.0, 2.0),
    ("abc", 0.0, 3.0, 4.0),
]

for x1_in, y1_in, x2_in, y2_in in p2_test_cases:
    if (
        not isinstance(x1_in, (int, float))
        or not isinstance(y1_in, (int, float))
        or not isinstance(x2_in, (int, float))
        or not isinstance(y2_in, (int, float))
    ):
        print("Error: invalid input")
    else:
        point_a = (float(x1_in), float(y1_in))
        point_b = (float(x2_in), float(y2_in))

        distance = (
            (point_b[0] - point_a[0]) ** 2 + (point_b[1] - point_a[1]) ** 2
        ) ** 0.5
        midpoint = (
            (point_a[0] + point_b[0]) / 2.0,
            (point_a[1] + point_b[1]) / 2.0,
        )

        print(f"Point A: {point_a}")
        print(f"Point B: {point_b}")
        print(f"Distance: {round(distance, 2)}")
        print(f"Midpoint: {midpoint}")


# CONCLUSIONS
"""
Lists allow dynamic data storage where elements can be appended or searched easily using in.
Tuples are ideal for immutable structured data, such as 2D coordinate pairs (x, y).
Slicing and index access enable quick retrieval of individual sequence elements.
Validating inputs before processing prevents runtime errors and maintains reliable execution.
Selecting between mutable lists and immutable tuples improves data structure clarity and safety.
"""


# REFERENCES
"""
1) Python Software Foundation. (2026). Built-in Types: Sequence Types — list, tuple, range. Python Documentation.
   https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range

2) Sweigart, A. (2020). Automate the Boring Stuff with Python: Practical Programming for Total Beginners. No Starch Press.

3) Lutz, M. (2013). Learning Python: Powerful Object-Oriented Programming. O'Reilly Media.

4) Severance, C. (2016). Python for Everybody: Exploring Data in Python 3. CreateSpace Independent Publishing Platform.

5) Real Python. (2026). Lists and Tuples in Python: A Complete Guide.
   https://realpython.com/python-lists-tuples/
"""
