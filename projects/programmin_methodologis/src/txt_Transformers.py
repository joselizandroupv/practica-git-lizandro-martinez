from Utils import clean_string, to_mxn

row = [
    {"name": "     ana    ", "active": True, "cash": "120.50"},
    {"name": "   LUIS ", "active": False, "cash": "00.00"},
    {"name": "    mara     ", "active": True, "cash": "99.99"},
]


def clean(row: dict) -> dict:
    return {
        "name": clean_string(row["name"]),
        "active": bool(row["active"]),
        "cash": to_mxn(row["cash"]),
    }


# List Comprehensions
clean_list = [clean(r) for r in row if r["active"] == True]
print("\n\n Lista Original:\n", row)
print("\n\n Lista Limpia:\n", clean_list)
