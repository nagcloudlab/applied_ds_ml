"""
LAB 04: REAL NEURAL NETWORK WITH NUMPY
=======================================
Lab 01: 1 neuron, pure math
Lab 02: 2 neurons + activation functions
Lab 03: 3 neurons (2+1), pure math
Lab 04: Full network, using NumPy (the tool real AI uses)

WHY NUMPY?
  In Labs 01-03 we wrote every multiply by hand.
  Real networks have 1000s of neurons. NumPy does ALL
  the multiplies at once: outputs = inputs @ weights + biases

PROBLEM: Predict if a person will buy a product based on:
  - Age (18-65), Salary (20k-100k), Hours on website (0-5)
"""

import numpy as np

# ============================================================
# STEP 1: DATA + WHY NUMPY
# ============================================================
print("=" * 55)
print("STEP 1: The data + why NumPy")
print("=" * 55)

print("""
  In Lab 03, one neuron was:
    score = input * weight + bias

  What if we have 3 inputs and 4 neurons?
  Without NumPy: 12 multiplications by hand!
  With NumPy:    outputs = inputs @ weights + biases  (ONE line!)
""")

# Will they buy? Based on: age, salary, hours_on_website
np.random.seed(42)

X_raw = np.array([
    [22, 25, 0.5], [25, 30, 0.3], [30, 35, 1.0], [35, 40, 0.5],
    [28, 45, 2.0], [45, 50, 0.2], [32, 55, 3.0], [40, 60, 2.5],
    [35, 65, 1.5], [28, 70, 4.0], [50, 55, 3.5], [38, 75, 2.0],
    [42, 80, 1.0], [33, 85, 3.5], [29, 90, 4.5], [45, 95, 2.0],
])

y = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

print(f"  {len(X_raw)} customers, 3 features each:\n")
print(f"  {'Age':>5} {'Salary(k)':>10} {'Hours':>6} {'Bought?':>8}")
print(f"  {'-'*35}")
for i in range(len(X_raw)):
    print(f"  {X_raw[i][0]:>5.0f} {X_raw[i][1]:>10.0f} {X_raw[i][2]:>6.1f} {'YES' if y[i] else 'NO':>8}")

input("\n  Press Enter to continue...")


# ============================================================
# STEP 2: NORMALIZE THE DATA
# ============================================================
print("\n" + "=" * 55)
print("STEP 2: Normalize the data")
print("=" * 55)

print("""
  Problem: Age is 18-65, Salary is 20k-100k, Hours is 0-5.
  The network would think salary is "more important" just
  because the NUMBERS are bigger.

  Solution: Scale everything to 0-1 range.
""")

X_min = X_raw.min(axis=0)
X_max = X_raw.max(axis=0)
X = (X_raw - X_min) / (X_max - X_min)

print(f"  Before: {X_raw[8].tolist()}  ->  After: [{X[8][0]:.2f}, {X[8][1]:.2f}, {X[8][2]:.2f}]")
print(f"  Now all values are between 0 and 1. Fair comparison!")

input("\n  Press Enter to build the network...")


# ============================================================
# STEP 3: BUILD THE NETWORK
# ============================================================
print("\n" + "=" * 55)
print("STEP 3: Build the network")
print("=" * 55)

print("""
  Our network:
    Input (3)  ->  Hidden (4 neurons)  ->  Output (1 neuron)

  Total weights to learn:
    Input->Hidden: 3 x 4 = 12 weights + 4 biases
    Hidden->Output: 4 x 1 = 4 weights + 1 bias
    Total: 21 learnable numbers!
""")

def sigmoid(x):
    return 1 / (1 + np.exp(-np.clip(x, -500, 500)))

np.random.seed(1)
W1 = np.random.randn(3, 4) * 0.5
b1 = np.zeros(4)
W2 = np.random.randn(4, 1) * 0.5
b2 = np.zeros(1)

print(f"  W1 shape: {W1.shape} (3 inputs -> 4 neurons)")
print(f"  W2 shape: {W2.shape} (4 neurons -> 1 output)")

input("\n  Press Enter to see the forward pass...")


# ============================================================
# STEP 4: FORWARD PASS (one customer)
# ============================================================
print("\n" + "=" * 55)
print("STEP 4: Forward pass (trace one customer)")
print("=" * 55)

customer = X[7]  # age=40, salary=60k, hours=2.5
actual = y[7]

z1 = customer @ W1 + b1
a1 = sigmoid(z1)
z2 = a1 @ W2 + b2
pred = sigmoid(z2)

print(f"\n  Customer: age=40, salary=60k, hours=2.5")
print(f"  Normalized: {customer}")
print(f"""
  Hidden layer (4 neurons computed AT ONCE with @):
    Neuron 1: {a1[0]:.4f}
    Neuron 2: {a1[1]:.4f}
    Neuron 3: {a1[2]:.4f}
    Neuron 4: {a1[3]:.4f}

  Output: sigmoid({z2[0]:.4f}) = {pred[0]:.4f}
  Prediction: {pred[0]:.1%} chance of buying
  (Random weights -> random prediction. Let's train!)
""")

input("  Press Enter to train...")


# ============================================================
# STEP 5: TRAINING
# ============================================================
print("\n" + "=" * 55)
print("STEP 5: Training the network")
print("=" * 55)

print("""
  Same 3 steps as Lab 03, but with matrices:
    1. FORWARD:  X @ W + b for ALL customers at once
    2. LOSS:     how wrong are we?
    3. BACKWARD: adjust weights (backprop with matrices)
""")

np.random.seed(1)
W1 = np.random.randn(3, 4) * 0.5
b1 = np.zeros(4)
W2 = np.random.randn(4, 1) * 0.5
b2 = np.zeros(1)

lr = 2.0
y_col = y.reshape(-1, 1)

print(f"  {'Round':>6} | {'Loss':>8} | {'Accuracy':>9} | Predictions")
print(f"  {'-'*60}")

for epoch in range(2001):
    # FORWARD
    z1 = X @ W1 + b1
    a1 = sigmoid(z1)
    z2 = a1 @ W2 + b2
    pred = sigmoid(z2)

    # LOSS
    loss = -np.mean(y_col * np.log(pred + 1e-7) + (1 - y_col) * np.log(1 - pred + 1e-7))

    # ACCURACY
    correct = np.sum((pred >= 0.5).flatten() == y)
    accuracy = correct / len(y) * 100

    # BACKWARD
    d2 = pred - y_col
    gW2 = a1.T @ d2 / len(X)
    gb2 = np.mean(d2, axis=0)
    d1 = (d2 @ W2.T) * a1 * (1 - a1)
    gW1 = X.T @ d1 / len(X)
    gb1 = np.mean(d1, axis=0)

    # UPDATE
    W2 -= lr * gW2
    b2 -= lr * gb2
    W1 -= lr * gW1
    b1 -= lr * gb1

    if epoch % 500 == 0 or epoch == 2000:
        preds_str = " ".join([f"{p[0]:.0f}" for p in (pred >= 0.5).astype(int)])
        actual_str = " ".join([f"{a}" for a in y])
        print(f"  {epoch:>6} | {loss:>8.4f} | {accuracy:>8.1f}% | [{preds_str}]")

print(f"         |          |           | [{actual_str}] (actual)")

input("\n  Press Enter to test on new customers...")


# ============================================================
# STEP 6: TEST ON NEW CUSTOMERS
# ============================================================
print(f"\n{'='*55}")
print("STEP 6: Predict new customers")
print("=" * 55)

new_customers = np.array([
    [24, 28, 0.5], [35, 50, 1.0], [30, 70, 3.0], [50, 40, 0.3],
    [28, 85, 4.0], [40, 60, 2.0], [55, 30, 0.2], [33, 95, 5.0],
])

X_new = (new_customers - X_min) / (X_max - X_min)

h = sigmoid(X_new @ W1 + b1)
predictions = sigmoid(h @ W2 + b2)

print(f"\n  {'Age':>5} {'Salary':>7} {'Hours':>6} {'Prob':>8} {'Will Buy?':>10}")
print(f"  {'-'*42}")
for i in range(len(new_customers)):
    age, sal, hrs = new_customers[i]
    prob = predictions[i][0]
    buy = "YES" if prob >= 0.5 else "NO"
    bar = "#" * int(prob * 20)
    print(f"  {age:>5.0f} {sal:>6.0f}k {hrs:>5.1f} {prob:>7.0%} {buy:>10}  {bar}")

print("""
  The network learned the pattern from data!
""")


# ============================================================
# SUMMARY
# ============================================================
print(f"{'='*55}")
print("SUMMARY - What you learned in Lab 04:")
print(f"{'='*55}")

print("""
  1. NumPy replaces hand-written math with matrix operations
     outputs = X @ W + b  (all neurons at once!)

  2. Same 3-step loop: forward -> loss -> backward
     But now it processes ALL data at once (vectorized)

  3. How far we've come:
     Lab 01: score = x*w + b             (1 neuron, by hand)
     Lab 03: 3 neurons, by hand          (30 lines of math)
     Lab 04: X @ W + b with NumPy        (10 lines!)

  Next: PyTorch - the real AI framework.
  It does everything we did, but even simpler:
    - Automatic backpropagation (no manual gradients!)
    - GPU acceleration (millions of neurons)
    - Pre-built layers, optimizers, loss functions
""")
