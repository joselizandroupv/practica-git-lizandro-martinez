# STUDENT INFORMATION / PORTADA
"""
Student Name: Jose Lizandro Villarreal Martinez
Student ID (Matricula): 2630116
Group: IM 1 - 2
"""

# EXECUTIVE SUMMARY / RESUMEN EJECUTIVO
"""
In Python, numeric data types include integers (int) for whole numbers and floating-point
numbers (float) for values requiring decimal precision. Boolean values (bool) represent
truth conditions as either True or False and are generated through relational comparisons.
Validating numerical ranges and preventing division by zero are essential safeguards
to ensure program stability, mathematical correctness, and prevent execution crashes.
This document presents six distinct programming problems covering unit conversions,
payroll calculations, discount rules, statistical analysis, loan eligibility,
and Body Mass Index (BMI) assessment using logical conditions and type casting.
"""


# PRINCIPLES AND BEST PRACTICES / PRINCIPIOS Y BUENAS PRÁCTICAS
"""
1. Use appropriate data types: use int for exact counts and float for real measurements.

2. Avoid repeating complex math: store intermediate calculations in descriptive variables.

3. Always validate inputs before operating: ensure values such as hours, salary, and
   measurements are non-negative, and prevent division by zero.

4. Follow clean naming conventions: use lower_snake_case for variables and UPPER_SNAKE_CASE
   for mathematical or policy constants.

5. Document boolean evaluations clearly: explain what true and false signify in each
   decision context (e.g., eligible vs. non-eligible).
"""


# PROBLEM 1: TEMPERATURE CONVERTER AND RANGE FLAG
"""
Description: 
Converts a temperature in Celsius to Fahrenheit and Kelvin scale values.
Additionally calculates a boolean flag indicating if the temperature is high (>= 30.0 °C).

Inputs:
- temp_c (float)

Outputs:
- Fahrenheit: <temp_f>
- Kelvin: <temp_k>
- High temperature: true / false

Validations:
- Verify input is a valid number.
- Prevent physical impossible temperatures below absolute zero in Kelvin (temp_k < 0.0).

Test cases:
1) Normal: 35.0 -> Fahrenheit: 95.0, Kelvin: 308.15, High temperature: true
2) Border: 30.0 -> Fahrenheit: 86.0, Kelvin: 303.15, High temperature: true
3) Error: -300.0 -> Error: invalid input
"""

print("--- PROBLEM 1 TESTS ---")

p1_test_inputs = [35.0, 30.0, -300.0]

for temp_c in p1_test_inputs:
    if not isinstance(temp_c, (int, float)):
        print("Error: invalid input")
    else:
        temp_c_val = float(temp_c)
        temp_k = temp_c_val + 273.15

        if temp_k < 0.0:
            print("Error: invalid input")
        else:
            temp_f = (temp_c_val * 9 / 5) + 32
            is_high_temperature = temp_c_val >= 30.0

            print(f"Fahrenheit: {round(temp_f, 2)}")
            print(f"Kelvin: {round(temp_k, 2)}")
            print(f"High temperature: {str(is_high_temperature).lower()}")


# PROBLEM 2: WORK HOURS AND OVERTIME PAYMENT
"""
Description: 
Calculates total weekly pay for a worker. Standard hours up to 40 are paid
at hourly_rate. Extra hours above 40 are paid at 150% rate.

Inputs:
- hours_worked (float)
- hourly_rate (float)

Outputs:
- Regular pay: <regular_pay>
- Overtime pay: <overtime_pay>
- Total pay: <total_pay>
- Has overtime: true / false

Validations:
- hours_worked >= 0
- hourly_rate > 0

Test cases:
1) Normal: hours_worked = 45.0, hourly_rate = 10.0 -> Regular: 400.0, Overtime: 75.0, Total: 475.0, Has overtime: true
2) Border: hours_worked = 40.0, hourly_rate = 10.0 -> Regular: 400.0, Overtime: 0.0, Total: 400.0, Has overtime: false
3) Error: hours_worked = -5.0, hourly_rate = 10.0 -> Error: invalid input
"""

print("\n--- PROBLEM 2 TESTS ---")

p2_test_cases = [
    (45.0, 10.0),
    (40.0, 10.0),
    (-5.0, 10.0),
]

for hours_worked, hourly_rate in p2_test_cases:
    if not isinstance(hours_worked, (int, float)) or not isinstance(
        hourly_rate, (int, float)
    ):
        print("Error: invalid input")
    else:
        hours = float(hours_worked)
        rate = float(hourly_rate)

        if hours < 0.0 or rate <= 0.0:
            print("Error: invalid input")
        else:
            regular_hours = min(hours, 40.0)
            overtime_hours = max(0.0, hours - 40.0)

            regular_pay = regular_hours * rate
            overtime_pay = overtime_hours * rate * 1.5
            total_pay = regular_pay + overtime_pay

            has_overtime = hours > 40.0

            print(f"Regular pay: {round(regular_pay, 2)}")
            print(f"Overtime pay: {round(overtime_pay, 2)}")
            print(f"Total pay: {round(total_pay, 2)}")
            print(f"Has overtime: {str(has_overtime).lower()}")


# PROBLEM 3: DISCOUNT ELIGIBILITY WITH BOOLEANS
"""
Description: 
Evaluates customer eligibility for a 10% store discount based on student status,
senior citizen status, or total purchase amount.

Inputs:
- purchase_total (float)
- is_student_text (string: "YES" or "NO")
- is_senior_text (string: "YES" or "NO")

Outputs:
- Discount eligible: true / false
- Final total: <final_total>

Validations:
- purchase_total >= 0.0
- Text flags must normalize to "YES" or "NO".

Test cases:
1) Normal: 500.0, "YES", "NO" -> Discount eligible: true, Final total: 450.0
2) Border: 1000.0, "NO", "NO" -> Discount eligible: true, Final total: 900.0
3) Error: -100.0, "MAYBE", "NO" -> Error: invalid input
"""

print("\n--- PROBLEM 3 TESTS ---")

p3_test_cases = [
    (500.0, "YES", "NO"),
    (1000.0, "NO", "NO"),
    (-100.0, "MAYBE", "NO"),
]

for purchase_total, is_student_text, is_senior_text in p3_test_cases:
    if not isinstance(purchase_total, (int, float)):
        print("Error: invalid input")
    else:
        total = float(purchase_total)
        s_txt = str(is_student_text).strip().upper()
        sr_txt = str(is_senior_text).strip().upper()

        if total < 0.0 or s_txt not in ["YES", "NO"] or sr_txt not in ["YES", "NO"]:
            print("Error: invalid input")
        else:
            is_student = s_txt == "YES"
            is_senior = sr_txt == "YES"

            discount_eligible = is_student or is_senior or (total >= 1000.0)

            if discount_eligible:
                final_total = total * 0.9
            else:
                final_total = total

            print(f"Discount eligible: {str(discount_eligible).lower()}")
            print(f"Final total: {round(final_total, 2)}")


# PROBLEM 4: BASIC STATISTICS OF THREE INTEGERS
"""
Description: 
Receives three integer numbers and computes sum, average, maximum,
minimum, and checks if all three numbers are even.

Inputs:
- n1 (int)
- n2 (int)
- n3 (int)

Outputs:
- Sum: <sum_value>
- Average: <average_value>
- Max: <max_value>
- Min: <min_value>
- All even: true / false

Validations:
- Inputs must be valid integer numbers (negative values allowed).

Test cases:
1) Normal: 4, 8, 12 -> Sum: 24, Average: 8.0, Max: 12, Min: 4, All even: true
2) Border: 0, 0, 0 -> Sum: 0, Average: 0.0, Max: 0, Min: 0, All even: true
3) Error: "abc", 5, 10 -> Error: invalid input
"""

print("\n--- PROBLEM 4 TESTS ---")

p4_test_cases = [
    (4, 8, 12),
    (0, 0, 0),
    ("abc", 5, 10),
]

for n1, n2, n3 in p4_test_cases:
    if type(n1) != int or type(n2) != int or type(n3) != int:
        print("Error: invalid input")
    else:
        num1 = int(n1)
        num2 = int(n2)
        num3 = int(n3)

        sum_value = num1 + num2 + num3
        average_value = sum_value / 3.0
        max_value = max(num1, num2, num3)
        min_value = min(num1, num2, num3)

        all_even = (num1 % 2 == 0) and (num2 % 2 == 0) and (num3 % 2 == 0)

        print(f"Sum: {sum_value}")
        print(f"Average: {round(average_value, 2)}")
        print(f"Max: {max_value}")
        print(f"Min: {min_value}")
        print(f"All even: {str(all_even).lower()}")


# PROBLEM 5: LOAN ELIGIBILITY (INCOME AND DEBT RATIO)
"""
Description: 
Assesses loan eligibility based on monthly income, monthly debt payments,
and credit score threshold criteria.

Inputs:
- monthly_income (float)
- monthly_debt (float)
- credit_score (int)

Outputs:
- Debt ratio: <debt_ratio>
- Eligible: true / false

Validations:
- monthly_income > 0.0 (prevents division by zero)
- monthly_debt >= 0.0
- credit_score >= 0

Test cases:
1) Normal: income = 10000.0, debt = 2000.0, score = 700 -> Debt ratio: 0.2, Eligible: true
2) Border: income = 8000.0, debt = 3200.0, score = 650 -> Debt ratio: 0.4, Eligible: true
3) Error: income = 0.0, debt = 1000.0, score = 700 -> Error: invalid input
"""

print("\n--- PROBLEM 5 TESTS ---")

p5_test_cases = [
    (10000.0, 2000.0, 700),
    (8000.0, 3200.0, 650),
    (0.0, 1000.0, 700),
]

for monthly_income, monthly_debt, credit_score in p5_test_cases:
    if (
        not isinstance(monthly_income, (int, float))
        or not isinstance(monthly_debt, (int, float))
        or type(credit_score) != int
    ):
        print("Error: invalid input")
    else:
        income = float(monthly_income)
        debt = float(monthly_debt)
        score = int(credit_score)

        if income <= 0.0 or debt < 0.0 or score < 0:
            print("Error: invalid input")
        else:
            debt_ratio = debt / income

            eligible = (income >= 8000.0) and (debt_ratio <= 0.4) and (score >= 650)

            print(f"Debt ratio: {round(debt_ratio, 2)}")
            print(f"Eligible: {str(eligible).lower()}")


# PROBLEM 6: BODY MASS INDEX (BMI) AND CATEGORY FLAG
"""
Description: 
Calculates Body Mass Index (BMI) using weight and height, generating boolean
flags for underweight, normal weight, and overweight categories.

Inputs:
- weight_kg (float)
- height_m (float)

Outputs:
- BMI: <bmi_rounded>
- Underweight: true / false
- Normal: true / false
- Overweight: true / false

Validations:
- weight_kg > 0.0
- height_m > 0.0

Test cases:
1) Normal: weight = 70.0, height = 1.75 -> BMI: 22.86, Normal: true
2) Border: weight = 59.2, height = 1.78 -> BMI: 18.68, Normal: true
3) Error: weight = -70.0, height = 1.75 -> Error: invalid input
"""

print("\n--- PROBLEM 6 TESTS ---")

p6_test_cases = [
    (70.0, 1.75),
    (59.2, 1.78),
    (-70.0, 1.75),
]

for weight_kg, height_m in p6_test_cases:
    if not isinstance(weight_kg, (int, float)) or not isinstance(
        height_m, (int, float)
    ):
        print("Error: invalid input")
    else:
        weight = float(weight_kg)
        height = float(height_m)

        if weight <= 0.0 or height <= 0.0:
            print("Error: invalid input")
        else:
            bmi = weight / (height * height)
            bmi_rounded = round(bmi, 2)

            is_underweight = bmi < 18.5
            is_normal = 18.5 <= bmi < 25.0
            is_overweight = bmi >= 25.0

            print(f"BMI: {bmi_rounded}")
            print(f"Underweight: {str(is_underweight).lower()}")
            print(f"Normal: {str(is_normal).lower()}")
            print(f"Overweight: {str(is_overweight).lower()}")


# CONCLUSIONS / CONCLUSIONES
"""
Integers and floating-point numbers work together to model real-world mathematical calculations.
Relational comparisons output boolean values (True or False), enabling programs to make logical
decisions through conditional branching.
Validating input boundaries and checking for zero values is essential to prevent mathematical
errors such as division by zero.
Combining conditions using 'and', 'or', and 'not' allows building clear evaluation systems.
These computational patterns form the backbone of financial, payroll, and medical decision algorithms.
"""


# REFERENCES / REFERENCIAS
"""
1) Python Software Foundation. (2026). Built-in Types: Numeric Types — int, float. Python Documentation.
   https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

2) Python Software Foundation. (2026). Boolean Values and Truth Value Testing. Python Documentation.
   https://docs.python.org/3/library/stdtypes.html#truth-value-testing

3) Sweigart, A. (2020). Automate the Boring Stuff with Python: Practical Programming for Total Beginners. No Starch Press.

4) Lutz, M. (2013). Learning Python: Powerful Object-Oriented Programming. O'Reilly Media.

5) Real Python. (2026). Python Booleans: Use Logical Operators and Conditional Statements.
   https://realpython.com/python-boolean/
"""
