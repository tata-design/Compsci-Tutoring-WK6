# ─────────────────────────────────────────
#  Week 6 – Functions
# ─────────────────────────────────────────

# Basic function
def greet(name):
    print(f"Hello, {name}!")

greet("Alex")
greet("Mr. Jonathan")

# Function with a return value
def add(a, b):
    return a + b

result = add(3, 7)
print("3 + 7 =", result)

# Function with a default parameter
def greet_with_title(name, title="Student"):
    print(f"Hello, {title} {name}!")

greet_with_title("Alex")
greet_with_title("Jonathan", "Mr.")

# ── Try it yourself ──────────────────────
# 1. Write a function called `multiply` that takes two numbers and returns
#    their product. Call it and print the result.
# 2. Write a function called `is_even` that returns True if a number is even,
#    and False otherwise.
