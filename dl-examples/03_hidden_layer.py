"""
LAB 03: WHY WE NEED LAYERS (From a line to a curve)
====================================================
In Lab 01, our single neuron could only draw a STRAIGHT LINE.
But real life isn't that simple.

PROBLEM: "How many hours should you study?"
  - Study 0-3 hrs  = FAIL  (too little)
  - Study 4-7 hrs  = PASS  (sweet spot)
  - Study 8-10 hrs = FAIL  (burnout, no rest, no revision)

A single neuron CANNOT solve this. We need TWO neurons
working together. Let's build it.
"""

import math
import random

def sigmoid(x):
    x = max(-500, min(500, x))
    return 1 / (1 + math.exp(-x))


# ============================================================
# STEP 1: SEE WHY A SINGLE NEURON FAILS
# ============================================================
print("=" * 55)
print("STEP 1: A single neuron CANNOT solve this")
print("=" * 55)

data = [
    (0, 0), (1, 0), (2, 0), (3, 0),   # too little -> FAIL
    (4, 1), (5, 1), (6, 1), (7, 1),   # sweet spot -> PASS
    (8, 0), (9, 0), (10, 0),          # burnout    -> FAIL
]

print("""
  The problem:
    Study 0-3 hrs  = FAIL  (too little)
    Study 4-7 hrs  = PASS  (sweet spot)
    Study 8-10 hrs = FAIL  (burnout)

  Visualized:
    Hours:  0  1  2  3  4  5  6  7  8  9  10
    Label:  .  .  .  .  #  #  #  #  .  .  .

  A single neuron draws ONE cutoff line.
  It can say "above 4 = PASS" but then 8,9,10 are also PASS.
  It CANNOT learn "between 4 and 7 = PASS".

  We need TWO cutoffs. That means TWO neurons.
""")

input("  Press Enter to see the solution...")


# ============================================================
# STEP 2: THE KEY IDEA - Two neurons = Two cutoffs
# ============================================================
print("\n" + "=" * 55)
print("STEP 2: The key idea")
print("=" * 55)

print("""
  We need TWO decisions combined:

    Neuron A: "Did they study ENOUGH?"      (hours >= 4?)
    Neuron B: "Did they study NOT TOO MUCH?" (hours <= 7?)

    Output:   "PASS only if BOTH say yes"

  Picture:

                    [Neuron A: enough?]
                   /                    \\
    [hours] ------                        ----> [Output: pass?]
                   \\                    /
                    [Neuron B: not too much?]

    Input            Hidden Layer            Output Layer
    (1 value)        (2 neurons)             (1 neuron)
""")

input("  Press Enter to build it by hand...")


# ============================================================
# STEP 3: Build it manually (hand-picked weights)
# ============================================================
print("\n" + "=" * 55)
print("STEP 3: Build the network by hand")
print("=" * 55)

print("""
  I'll CHOOSE weights so you see exactly how it works.
  Then we'll let the computer learn them.

  The trick: use LARGE weights for sharp yes/no boundaries.
""")

# Neuron A: "enough study?" -> turns ON around 4 hours
wA = 20.0
bA = -8.0

# Neuron B: "not too much?" -> turns OFF around 8 hours
wB = -20.0
bB = 15.0

# Output: "PASS only if BOTH A and B say yes"
wOA = 20.0
wOB = 20.0
bO = -30.0

print(f"  Neuron A (enough?):    w={wA:>5.0f}, b={bA:>5.0f}")
print(f"  Neuron B (not too much?): w={wB:>5.0f}, b={bB:>5.0f}")
print(f"  Output (both agree?):  wA={wOA:.0f}, wB={wOB:.0f}, b={bO:.0f}")

print(f"\n  Let's trace through 3 students:\n")

for hours in [2, 5, 9]:
    x = hours / 10

    zA = x * wA + bA
    a = sigmoid(zA)

    zB = x * wB + bB
    b_val = sigmoid(zB)

    zO = a * wOA + b_val * wOB + bO
    output = sigmoid(zO)

    correct = "PASS" if 4 <= hours <= 7 else "FAIL"
    pred = "PASS" if output >= 0.5 else "FAIL"

    print(f"  --- Student: {hours} hours ---")
    print(f"    Neuron A (enough?):      {x}*{wA:.0f} + ({bA:.0f}) = {zA:>5.1f} -> sigmoid = {a:.2f} {'YES' if a > 0.5 else 'NO'}")
    print(f"    Neuron B (not too much?): {x}*{wB:.0f} + {bB:.0f}  = {zB:>5.1f} -> sigmoid = {b_val:.2f} {'YES' if b_val > 0.5 else 'NO'}")
    print(f"    Output:  {a:.2f}*{wOA:.0f} + {b_val:.2f}*{wOB:.0f} + ({bO:.0f}) = {zO:>6.1f} -> sigmoid = {output:.2f}")
    print(f"    Prediction: {pred}  (correct: {correct}) {'OK!' if pred == correct else 'WRONG'}")
    print()

hand_wrong = sum(1 for h in range(11)
    if (sigmoid(sigmoid(h/10*wA+bA)*wOA + sigmoid(h/10*wB+bB)*wOB + bO) >= 0.5) != (4 <= h <= 7))
print(f"  {11-hand_wrong}/11 correct! The two neurons capture the sweet spot!")
print(f"\n  But we CHOSE these weights. Can the network LEARN them?")

input("\n  Press Enter to see it learn...")


# ============================================================
# STEP 4: The network learns by itself
# ============================================================
print("\n" + "=" * 55)
print("STEP 4: Let the network learn (backpropagation)")
print("=" * 55)

print("""
  FORWARD:  Input -> Hidden neurons -> Output -> Prediction
  ERROR:    How wrong was the prediction?
  BACKWARD: Adjust weights layer by layer.
            Errors flow BACKWARD = "backpropagation"
""")

random.seed(42)
w_h1 =  2.0
b_h1 = random.uniform(-1, 1)
w_h2 = -2.0
b_h2 = random.uniform(-1, 1)

w_o1 = random.uniform(0.5, 1.5)
w_o2 = random.uniform(0.5, 1.5)
b_o  = random.uniform(-1, 0)

lr = 5.0

print(f"  {'Round':>6} | {'Correct':>8} | Predictions                     | Status")
print(f"  {'-'*72}")

for epoch in range(5001):
    correct = 0

    for hours, actual in data:
        x = hours / 10

        # ---- FORWARD ----
        z_h1 = x * w_h1 + b_h1
        a_h1 = sigmoid(z_h1)

        z_h2 = x * w_h2 + b_h2
        a_h2 = sigmoid(z_h2)

        z_o = a_h1 * w_o1 + a_h2 * w_o2 + b_o
        pred = sigmoid(z_o)

        if (pred >= 0.5) == (actual == 1):
            correct += 1

        # ---- BACKWARD ----
        d_o = pred - actual
        d_h1 = d_o * w_o1 * a_h1 * (1 - a_h1)
        d_h2 = d_o * w_o2 * a_h2 * (1 - a_h2)

        # ---- UPDATE ----
        w_o1 -= lr * d_o * a_h1
        w_o2 -= lr * d_o * a_h2
        b_o  -= lr * d_o

        w_h1 -= lr * d_h1 * x
        b_h1 -= lr * d_h1
        w_h2 -= lr * d_h2 * x
        b_h2 -= lr * d_h2

    accuracy = correct / len(data) * 100

    if epoch % 1000 == 0 or epoch == 5000:
        preds = ""
        for h in range(11):
            xn = h / 10
            ah1 = sigmoid(xn * w_h1 + b_h1)
            ah2 = sigmoid(xn * w_h2 + b_h2)
            p = sigmoid(ah1 * w_o1 + ah2 * w_o2 + b_o)
            preds += " #" if p >= 0.5 else " ."
        status = "LEARNING..." if accuracy < 100 else "SOLVED!"
        print(f"  {epoch:>6} | {correct:>5}/{len(data):>2} | {preds} | {status}")

print(f"         |          | (goal: .  .  .  .  #  #  #  #  .  .  .)")

input("\n  Press Enter to see the comparison...")


# ============================================================
# STEP 5: Single neuron vs Neural Network
# ============================================================
print(f"\n{'='*55}")
print("STEP 5: Single neuron vs Neural Network")
print("=" * 55)

# Quick single neuron (no training loop shown - just result)
random.seed(42)
sw, sb = random.uniform(-1, 1), random.uniform(-1, 1)
for epoch in range(1000):
    for hours, actual in data:
        x = hours / 10
        pred = sigmoid(x * sw + sb)
        error = pred - actual
        sw -= 1.0 * error * x
        sb -= 1.0 * error

print(f"""
  Problem: PASS only if studying 4-7 hours

  Hours:        0  1  2  3  4  5  6  7  8  9  10
  Actual:       .  .  .  .  #  #  #  #  .  .  .
""")

print(f"  1 Neuron:     ", end="")
one_correct = 0
for h in range(11):
    p = sigmoid(h/10 * sw + sb)
    c = '#' if p >= 0.5 else '.'
    a = '#' if 4 <= h <= 7 else '.'
    if c == a: one_correct += 1
    print(f" {c} ", end="")
print(f"  ({one_correct}/11 correct)")

print(f"  2+1 Network:  ", end="")
two_correct = 0
for h in range(11):
    ah1 = sigmoid(h/10 * w_h1 + b_h1)
    ah2 = sigmoid(h/10 * w_h2 + b_h2)
    p = sigmoid(ah1 * w_o1 + ah2 * w_o2 + b_o)
    c = '#' if p >= 0.5 else '.'
    a = '#' if 4 <= h <= 7 else '.'
    if c == a: two_correct += 1
    print(f" {c} ", end="")
print(f"  ({two_correct}/11 correct)")

print(f"""
  Single neuron: ONE cutoff -> fails
  Neural network: TWO hidden neurons = TWO cutoffs -> solved!
""")


# ============================================================
# SUMMARY
# ============================================================
print(f"{'='*55}")
print("SUMMARY - What you learned in Lab 03:")
print(f"{'='*55}")

print("""
  1. SINGLE neuron = only a STRAIGHT LINE
     Fails on: "middle is best" type problems.

  2. TWO hidden neurons = TWO boundaries
     Neuron A: "is it above the lower limit?"
     Neuron B: "is it below the upper limit?"
     Output:   "both yes? Then PASS!"

  3. BACKPROPAGATION in 4 bullets:
     - Compute output error (prediction - actual)
     - Fix output weights (same as Lab 01)
     - Split blame to hidden neurons (by their connection weight)
     - Fix hidden weights (each neuron gets its share of blame)
     That's it! "Send the error backward, layer by layer."

  4. More neurons = more boundaries = more complex patterns
     2 neurons  -> capture a range (this lab)
     100 neurons -> can learn almost anything!

  Next: NumPy matrix math - doing 1000 neurons in 1 line.
""")
