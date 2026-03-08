# ============================================================
# WEEK 6 ASSIGNMENT — Sensors & Decisions (Part 2)
# Taylor's Copy
# ============================================================
#
# WEEK 5 RECAP:
#   - if / elif / else with a single sensor
#   - Reactive robot: read sensor -> decide -> act
#   - Sensor simulation using random.randint()
#
# THIS WEEK'S NEW CONCEPTS:
#   - Compound boolean expressions (and, or, not)
#   - Truth tables
#   - Nested conditionals with multiple sensors
#   - Priority ordering in decision trees
#
# HOMEWORK: Complete all three TODOs below.
# TIP: Sketch each problem on paper FIRST before coding.
#      That's calsdvled pseudocode — it's exactly what the
#      AP Create Task asks you to document!
# ============================================================

import random


# ============================================================
# SENSOR SIMULATOR (same as Week 5 — already done for you)
# ============================================================

def read_distance_sensor():
    """Returns simulated distance reading in inches (0–100)"""
    return random.randint(0, 100)

def read_line_sensor():
    """Returns simulated line reflectance (0 = on line, 100 = off)"""
    return random.randint(0, 100)

def read_color_sensor():
    """Returns simulated color: 'red', 'green', or 'none'"""
    return random.choice(["red", "green", "none", "none", "none"])


# ============================================================
# TODO 1 — TRUTH TABLE EVALUATOR
# ============================================================
# A truth table lists every combination of True/False for
# two boolean variables and shows what the combined
# expression evaluates to.
#
# Your job: complete the function below so it prints a
# truth table for this safety expression:
#
#   can_drive = NOT obstacle_ahead AND NOT battery_low
#
# Expected output should look like:
#
#   obstacle_ahead | battery_low | can_drive
#   ------------------------------------------------
#   False          | False       | True
#   False          | True        | False
#   True           | False       | False
#   True           | True        | False
#
# AP Connection: Truth tables appear on the AP exam.
# Being able to complete one quickly is a real skill.
# ============================================================

def print_truth_table():
    """
    Prints a truth table for:
    can_drive = NOT obstacle_ahead AND NOT battery_low
    """
    print("TODO 1: Truth Table")
    print(f"{'obstacle_ahead':<16} {'battery_low':<14} {'can_drive'}")
    print("-" * 44)
    for obstacle_ahead in [False, True]:
        for battery_low in [False, True]:
            can_drive = (not obstacle_ahead) and (not battery_low)
            print(f"{str(obstacle_ahead):<16} {str(battery_low):<14} {can_drive}")

    print()
    print("Key insight: robot can ONLY move when BOTH are False.")
    print("One problem = no movement. That's the AND requirement.")
    print()

print_truth_table()


# ============================================================
# TODO 2 — MULTI-SENSOR DECISION FUNCTION
# ============================================================
# Complete the function below so the robot makes the right
# decision based on ALL THREE sensors simultaneously.
#
# Rules (in priority order — most important first):
#
#   Priority 1: distance < 6
#               -> return "EMERGENCY STOP"
#
#   Priority 2: distance < 12 AND color == "red"
#               -> return "DANGER ZONE — stop and alert"
#
#   Priority 3: color == "red"  (but distance is >= 12)
#               -> return "HAZARD — slow to 25%"
#
#   Priority 4: line_val > 60
#               -> return "OFF LINE — search for line"
#
#   Priority 5: distance < 20  (nothing else triggered above)
#               -> return "CAUTION — obstacle ahead"
#
#   Priority 6: none of the above
#               -> return "CLEAR — full speed patrol"
#
# HINT: Think about why distance must be checked BEFORE color.
#       What would happen if you checked color first?
# ============================================================

def multi_sensor_decision(distance, line_val, color):
    """
    Makes a robot decision based on three sensor inputs.
    
    Parameters:
        distance (int): inches to nearest object (0-100)
        line_val (int): 0 = on line, 100 = completely off line
        color    (str): "red", "green", or "none"
    
    Returns:
        str: decision string describing what the robot should do
    """

    # TODO 2: Write the if/elif/else chain using the rules above.
    # Remember: check the MOST CRITICAL condition first.

    if distance < 6:
        return "EMERGENCY STOP"
    elif color == "red" and distance < 12:
        return "DANGER ZONE — stop and alert"
    elif color == "red" and distance >= 12:
        return "HAZARD — slow to 25%"
    elif line_val > 60:
        return "OFF LINE — search for line"
    elif distance < 20:
        return "CAUTION — obstacle ahead"
    else:
        return "CLEAR — full speed patrol"


# --- Test your function with these cases ---
# Run this to check your work. You should know what each answer should be.

print("TODO 2: Multi-Sensor Decision Tests")
print(f"{'Test':<30} {'Your Answer'}")
print("-" * 55)

test_cases = [
    (3,  10, "none",  "Obstacle 3in away"),
    (8,  15, "red",   "8in away + red marker"),
    (20, 10, "red",   "20in away + red marker"),
    (50, 80, "none",  "Off line, path clear"),
    (15, 20, "green", "15in away, green marker"),
    (50, 10, "none",  "All sensors clear"),
]

for dist, line, color, description in test_cases:
    result = multi_sensor_decision(dist, line, color)
    print(f"{description:<30} {result}")

print()


# ============================================================
# TODO 3 — WAREHOUSE PATROL DECISION TREE
# ============================================================
# A robot patrols a warehouse and must make decisions
# based on what it detects.
#
# STEP 1: On paper, draw a flowchart for these rules:
#
#   - If obstacle within 6 inches:
#       Stop immediately
#   - Else if battery below 15%:
#       Return to charging dock (regardless of other sensors)
#   - Else if green object detected AND distance > 10:
#       Collect the object
#   - Else if red marker detected:
#       Log location and continue slowly
#   - Else:
#       Continue patrol at normal speed
#
# STEP 2: Implement the decision function below.
# STEP 3: Run the simulation and answer the reflection questions.
#
# AP Connection: This is a decision tree — it's the same
# concept tested in AP CSP Big Idea 3 algorithm questions.
# ============================================================

def patrol_decision(distance, battery_pct, color):
    """
    Makes patrol decisions for a warehouse robot.
    
    Parameters:
        distance    (int): inches to nearest object
        battery_pct (int): battery percentage 0-100
        color       (str): "red", "green", or "none"
    
    Returns:
        str: action the robot should take
    """

    # TODO 3a: Implement the decision tree described above.
    if distance < 6:
        return "STOP IMMEDIATELY"
    elif battery_pct < 15:
        return "RETURN TO CHARGING DOCK"
    elif color == "green" and distance > 10:
        return "COLLECT OBJECT"
    elif color == "red":
        return "LOG LOCATION AND CONTINUE SLOWLY"
    else:
        return "CONTINUE PATROL AT NORMAL SPEED"

# --- Simulation: Run patrol for 20 steps ---
def run_patrol_simulation(steps=20):
    """Run the patrol robot and log all decisions."""
    log = []
    for step in range(1, steps + 1):

        # Simulate sensors
        dist    = read_distance_sensor()
        color   = read_color_sensor()
        battery = random.randint(10, 100)   # Battery drains over time in real life

        action = patrol_decision(dist, battery, color)

        log.append({
            "step"   : step,
            "dist"   : dist,
            "battery": battery,
            "color"  : color,
            "action" : action
        })
    return log


print("TODO 3: Warehouse Patrol Simulation (20 steps)")
print(f"{'Step':<5} {'Dist':>5} {'Bat%':>5} {'Color':<8} {'Action'}")
print("-" * 55)

patrol_log = run_patrol_simulation(20)
for entry in patrol_log:
    print(f"  {entry['step']:<3} {entry['dist']:>5}in "
          f"{entry['battery']:>4}%  {entry['color']:<8} {entry['action']}")

print()

# --- Reflection Questions ---
print("Reflection Questions:")
print("1. Which sensor triggered the most actions? Why do you think that is?")
print ("   (Hint: Look at the distribution of sensor readings in your log.)")
print("2. Did you see any cases where the order of conditions in your code mattered?")
print("3. How would you modify the decision tree if the robot had a new sensor (e.g., temperature)?")
