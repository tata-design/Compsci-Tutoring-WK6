# ─────────────────────────────────────────
#  Week 6 – Control Flow (if / elif / else)
# ─────────────────────────────────────────

score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}  →  Grade: {grade}")

# --- Loops ---

# while loop
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

# range()
for i in range(1, 6):
    print("Number:", i)

# ── Try it yourself ──────────────────────
# 1. Change `score` to different values and see which grade prints.
# 2. Write a for loop that prints the numbers 10, 20, 30, 40, 50.
