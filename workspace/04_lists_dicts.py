# ─────────────────────────────────────────
#  Week 6 – Lists & Dictionaries
# ─────────────────────────────────────────

# --- Lists ---
students = ["Alice", "Bob", "Charlie", "Diana"]

print("All students:", students)
print("First student:", students[0])
print("Last student:", students[-1])

# Adding and removing items
students.append("Eve")
print("After append:", students)

students.remove("Bob")
print("After remove:", students)

print("Number of students:", len(students))

# --- Dictionaries ---
person = {
    "name": "Alex",
    "age": 16,
    "grade": "11th"
}

print("\nName:", person["name"])
print("Age:", person["age"])

# Adding a new key
person["hobby"] = "coding"
print("Updated person:", person)

# Iterating over a dictionary
for key, value in person.items():
    print(f"  {key}: {value}")

# ── Try it yourself ──────────────────────
# 1. Create a list of your 5 favorite movies and print each one with a loop.
# 2. Create a dictionary describing yourself (name, age, favorite subject).
