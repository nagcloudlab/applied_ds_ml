"""
LAB 01: THE SINGLE NEURON
=========================
Imagine you are a TEACHER deciding if a student will pass or fail.
You look at 2 things:
  - How many hours did they STUDY?
  - How many hours did they SLEEP?

A neuron does the EXACT same thing. Let's build it step by step.
"""

# ============================================================
# STEP 1: A neuron is just MULTIPLY + ADD
# ============================================================
print("=" * 55)
print("STEP 1: A neuron is just multiply + add")
print("=" * 55)

# You are the teacher. A student comes to you:
hours_studied = 7
hours_slept = 6

# As a teacher, you think:
#   "Studying is VERY important, sleeping is SOMEWHAT important"
#
# So you give IMPORTANCE SCORES (these are called WEIGHTS):
weight_study = 3    # studying is 3x important
weight_sleep = 1    # sleeping is 1x important

# You also have a STARTING MOOD (this is called BIAS):
#   negative mood = "I'll fail you unless you prove yourself"
bias = -15

# Now the neuron computes:
score = (hours_studied * weight_study) + (hours_slept * weight_sleep) + bias

print(f"""
  Student: studied {hours_studied} hrs, slept {hours_slept} hrs

  Neuron calculation:
    (study * importance) + (sleep * importance) + mood
    ({hours_studied}     *  {weight_study})          + ({hours_slept}     * {weight_sleep})          + ({bias})
    = {hours_studied * weight_study}                + {hours_slept * weight_sleep}                + ({bias})
    = {score}

  Score = {score}
  Positive score = PASS, Negative score = FAIL
  Result: {"PASS" if score > 0 else "FAIL"}
""")

# Let's try another student:
print("  Let's try a lazy student: studied 2 hrs, slept 3 hrs")
score2 = (2 * weight_study) + (3 * weight_sleep) + bias
print(f"    Score = (2 * {weight_study}) + (3 * {weight_sleep}) + ({bias}) = {score2}")
print(f"    Result: {"PASS" if score2 > 0 else "FAIL"}")

print("""
  THATS IT! A neuron = multiply each input by its weight, add bias.
  Nothing more. Just multiply + add.
""")
input("  Press Enter to continue to Step 2...")


# ============================================================
# STEP 2: But we want PROBABILITY, not just yes/no
# ============================================================
print("\n" + "=" * 55)
print("STEP 2: Converting score to probability (sigmoid)")
print("=" * 55)

print("""
  Problem: Our score can be any number (-100, 0, 50, 999...)
  We want: a probability between 0% and 100%

  Solution: SIGMOID function
  It squishes ANY number into 0 to 1:

    Big positive (like +10) --> close to 1.0 (confident PASS)
    Big negative (like -10) --> close to 0.0 (confident FAIL)
    Zero                    --> exactly  0.5 (50-50, unsure)

  Formula: sigmoid(x) = 1 / (1 + 2.718^(-x))
  Don't memorize - just know it SQUISHES numbers to 0-1.
""")

import math

def sigmoid(x):
    """Squish any number to 0-1 range."""
    x = max(-500, min(500, x))
    return 1 / (1 + math.exp(-x))

# Show it:
print("  Let's see it work:")
print(f"    sigmoid(-10) = {sigmoid(-10):.4f}  (very negative -> near 0)")
print(f"    sigmoid( -2) = {sigmoid(-2):.4f}  (negative -> below 0.5)")
print(f"    sigmoid(  0) = {sigmoid(0):.4f}  (zero -> exactly 0.5)")
print(f"    sigmoid(  2) = {sigmoid(2):.4f}  (positive -> above 0.5)")
print(f"    sigmoid( 10) = {sigmoid(10):.4f}  (very positive -> near 1)")

# Now our neuron with sigmoid:
print(f"""
  Our good student (studied 7, slept 6):
    Score = {score}
    Probability = sigmoid({score}) = {sigmoid(score):.4f}
    = {sigmoid(score)*100:.1f}% chance of passing --> PASS

  Our lazy student (studied 2, slept 3):
    Score = {score2}
    Probability = sigmoid({score2}) = {sigmoid(score2):.4f}
    = {sigmoid(score2)*100:.1f}% chance of passing --> FAIL
""")

input("  Press Enter to continue to Step 3...")


# ============================================================
# STEP 3: Complete neuron function
# ============================================================
print("\n" + "=" * 55)
print("STEP 3: Our complete neuron in 3 lines")
print("=" * 55)

def neuron(study, sleep, w1, w2, b):
    """A complete neuron. That's it. 3 lines."""
    score = (study * w1) + (sleep * w2) + b    # multiply + add
    probability = sigmoid(score)                # squish to 0-1
    return probability

# Test with our weights
w1, w2, b = 3, 1, -15

print(f"\n  Weights: study_importance={w1}, sleep_importance={w2}, mood={b}")
print(f"\n  Testing different students:\n")
print(f"  {'Studied':>8} {'Slept':>6} {'Probability':>12} {'Verdict':>8}")
print(f"  {'-'*40}")

students = [(1,1), (2,3), (4,4), (5,5), (6,4), (7,6), (8,7), (9,9)]
for study, sleep in students:
    prob = neuron(study, sleep, w1, w2, b)
    verdict = "PASS" if prob >= 0.5 else "FAIL"
    print(f"  {study:>8} {sleep:>6} {prob:>11.1%} {verdict:>8}")

print("""
  But WAIT - we CHOSE the weights (3, 1, -15) by hand.
  What if we're wrong? What if sleep matters more?

  We need the neuron to FIND the best weights BY ITSELF.
  That's called LEARNING. Let's do it.
""")

input("  Press Enter to continue to Step 4...")


# ============================================================
# STEP 4: How does a neuron LEARN? (simplest explanation)
# ============================================================
print("\n" + "=" * 55)
print("STEP 4: How learning works (3 simple ideas)")
print("=" * 55)

print("""
  Imagine you're throwing darts at a target:

  IDEA 1: MEASURE THE ERROR
    "How far was my dart from the bullseye?"
    Error = prediction - actual_answer

  IDEA 2: FIGURE OUT WHICH WAY TO ADJUST
    "Was I too high? Then aim lower."
    "Was I too low? Then aim higher."
    This is called the GRADIENT (fancy word for "direction to fix")

  IDEA 3: MAKE A SMALL ADJUSTMENT
    Don't overcorrect! Move just a little bit.
    new_weight = old_weight - small_step * error_direction

  That's all learning is: Measure error, find direction, adjust a little.
  Repeat 100s of times and the weights get better and better.

  Let's see it happen with real numbers...
""")

input("  Press Enter to see learning in action...")


# ============================================================
# STEP 5: Watch the neuron learn (with real numbers!)
# ============================================================
print("\n" + "=" * 55)
print("STEP 5: Watching the neuron learn")
print("=" * 55)

# Our training data: students we KNOW the answer for
# (studied, slept, actually_passed?)
data = [
    (1, 1, 0),   # FAIL
    (2, 1, 0),   # FAIL
    (1, 3, 0),   # FAIL
    (2, 5, 0),   # FAIL
    (3, 2, 0),   # FAIL
    (3, 6, 0),   # FAIL
    (5, 2, 0),   # FAIL
    (5, 5, 1),   # PASS
    (6, 4, 1),   # PASS
    (6, 7, 1),   # PASS
    (7, 5, 1),   # PASS
    (7, 8, 1),   # PASS
    (8, 3, 1),   # PASS
    (8, 7, 1),   # PASS
    (9, 6, 1),   # PASS
    (9, 9, 1),   # PASS
]

# Start with random weights (the neuron knows NOTHING)
import random
random.seed(42)
w1 = random.uniform(-1, 1)    # random importance for study
w2 = random.uniform(-1, 1)    # random importance for sleep
b  = random.uniform(-1, 1)    # random mood

learning_rate = 0.1   # how big each adjustment is

print(f"\n  Starting weights (random, knows nothing):")
print(f"    w1 = {w1:.4f}, w2 = {w2:.4f}, b = {b:.4f}")
print(f"    Learning rate = {learning_rate}")

print(f"\n  Let me show the FIRST learning step in detail:\n")

# --- ONE DETAILED LEARNING STEP ---
study, sleep, actual = data[7]   # student who studied 5, slept 5, PASSED
print(f"  Student: studied={study}, slept={sleep}, actual=PASS(1)")

# Forward: make prediction
score = (study/10 * w1) + (sleep/10 * w2) + b
pred = sigmoid(score)
print(f"  Prediction = {pred:.4f} ({pred*100:.1f}%)")

# Error
error = pred - actual
print(f"  Error = prediction - actual = {pred:.4f} - {actual} = {error:.4f}")
if error < 0:
    print(f"  (Negative error = we predicted too LOW, need to push UP)")
else:
    print(f"  (Positive error = we predicted too HIGH, need to push DOWN)")

# Gradients (direction to adjust)
grad_w1 = error * (study / 10)
grad_w2 = error * (sleep / 10)
grad_b  = error
print(f"\n  How much to adjust each weight:")
print(f"    w1 direction = error * input1 = {error:.4f} * {study/10:.1f} = {grad_w1:.4f}")
print(f"    w2 direction = error * input2 = {error:.4f} * {sleep/10:.1f} = {grad_w2:.4f}")
print(f"    b  direction = error          = {grad_b:.4f}")

# Update
w1_new = w1 - learning_rate * grad_w1
w2_new = w2 - learning_rate * grad_w2
b_new  = b  - learning_rate * grad_b
print(f"\n  Update weights (old - learning_rate * direction):")
print(f"    w1: {w1:.4f} - {learning_rate} * {grad_w1:.4f} = {w1_new:.4f}")
print(f"    w2: {w2:.4f} - {learning_rate} * {grad_w2:.4f} = {w2_new:.4f}")
print(f"    b:  {b:.4f} - {learning_rate} * {grad_b:.4f}  = {b_new:.4f}")
print(f"\n  Weights got slightly adjusted! Repeat this 1000s of times...")

input("\n  Press Enter to see full training...")


# ============================================================
# STEP 6: Full training - watch accuracy improve
# ============================================================
print("\n" + "=" * 55)
print("STEP 6: Full training (watch it get smarter)")
print("=" * 55)

# Reset
random.seed(42)
w1 = random.uniform(-1, 1)
w2 = random.uniform(-1, 1)
b  = random.uniform(-1, 1)
learning_rate = 0.5

print(f"\n  {'Round':>6} | {'Correct':>8} | {'Accuracy':>9} | {'w1':>7} | {'w2':>7} | {'b':>7}")
print(f"  {'-'*58}")

for epoch in range(201):
    correct = 0

    for study, sleep, actual in data:
        # Normalize inputs to 0-1
        x1 = study / 10
        x2 = sleep / 10

        # FORWARD: predict
        score = (x1 * w1) + (x2 * w2) + b
        pred = sigmoid(score)

        # Count accuracy
        if (pred >= 0.5 and actual == 1) or (pred < 0.5 and actual == 0):
            correct += 1

        # BACKWARD: compute error and adjust
        error = pred - actual
        w1 -= learning_rate * error * x1
        w2 -= learning_rate * error * x2
        b  -= learning_rate * error

    accuracy = correct / len(data) * 100

    if epoch % 25 == 0 or epoch == 200:
        print(f"  {epoch:>6} | {correct:>5}/{len(data):>2} | {accuracy:>8.1f}% | {w1:>7.2f} | {w2:>7.2f} | {b:>7.2f}")

print(f"""
  The neuron started knowing NOTHING (random weights).
  After 200 rounds of practice, it learned:
    - w1 = {w1:.2f} (how much studying matters)
    - w2 = {w2:.2f} (how much sleeping matters)
    - b  = {b:.2f} (default tendency)
""")

if w1 > w2:
    print(f"  INSIGHT: Studying (w1={w1:.1f}) matters MORE than sleeping (w2={w2:.1f})!")
else:
    print(f"  INSIGHT: Sleeping (w2={w2:.1f}) matters MORE than studying (w1={w1:.1f})!")

if b < 0:
    print(f"  INSIGHT: Negative bias ({b:.1f}) = default is FAIL (must earn a pass)")

input("\n  Press Enter to test the trained neuron...")


# ============================================================
# STEP 7: Test the trained neuron on NEW students
# ============================================================
print("\n" + "=" * 55)
print("STEP 7: Test on new students (never seen before!)")
print("=" * 55)

test = [
    (1, 1, "No study, no sleep"),
    (3, 3, "Low both"),
    (5, 5, "Medium both"),
    (7, 6, "Good study, good sleep"),
    (9, 8, "Great both"),
    (8, 1, "Great study, no sleep"),
    (1, 9, "No study, great sleep"),
    (10, 10, "Perfect"),
]

print(f"\n  {'Studied':>8} {'Slept':>6} {'Chance':>8} {'Verdict':>8}  Why?")
print(f"  {'-'*65}")

for study, sleep, desc in test:
    prob = sigmoid((study/10 * w1) + (sleep/10 * w2) + b)
    verdict = "PASS" if prob >= 0.5 else "FAIL"
    bar = "#" * int(prob * 20)
    print(f"  {study:>8} {sleep:>6} {prob:>7.0%} {verdict:>8}  {bar:<20} {desc}")


# ============================================================
# STEP 8: SEE the decision boundary
# ============================================================
print(f"\n\n{'='*55}")
print("STEP 8: The decision boundary")
print("=" * 55)
print("""
  The neuron draws an invisible LINE across all possible students.
  Above the line = PASS, Below the line = FAIL.
  . = FAIL    # = PASS
""")

print("        Sleep: 0  1  2  3  4  5  6  7  8  9 10")
print("  Study")
for study in range(10, -1, -1):
    row = f"   {study:>2}         "
    for sleep in range(11):
        prob = sigmoid((study/10 * w1) + (sleep/10 * w2) + b)
        row += " # " if prob >= 0.5 else " . "
    print(row)


# ============================================================
# SUMMARY
# ============================================================
print(f"""

{'='*55}
SUMMARY - What you learned:
{'='*55}

  A NEURON does 3 things:

    1. MULTIPLY each input by a weight (importance)
       score = study * w1 + sleep * w2

    2. ADD a bias (default tendency)
       score = score + b

    3. SQUISH to 0-1 using sigmoid
       probability = sigmoid(score)

  LEARNING means:
    1. Make a prediction
    2. Check how wrong you were (error)
    3. Adjust weights a tiny bit to be less wrong
    4. Repeat 1000s of times

  LIMITATION:
    A single neuron can only draw a STRAIGHT line.
    Real problems need CURVES.
    --> Next lab: combine multiple neurons = curves!
""")
