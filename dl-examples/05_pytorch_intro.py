"""
LAB 05: PYTORCH - The Real Deal
================================
Lab 01-03: pure math               (understand the concepts)
Lab 04:    NumPy                    (understand matrix math)
Lab 05:    PyTorch                  (how pros do it)

WHAT PYTORCH GIVES US:
  1. No manual gradients - it computes them AUTOMATICALLY
  2. Pre-built layers - just say "give me 4 neurons"
  3. Pre-built optimizers - SGD, Adam (smarter learning)
  4. GPU support - train on graphics card (1000x faster)

PROBLEM: Same as Lab 04 (predict buying) but with PyTorch.
         You'll see how LITTLE code is needed.
"""

import torch
import torch.nn as nn
import numpy as np

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"  Using device: {device}")

# ============================================================
# STEP 1: PYTORCH BASICS (Tensors + Autograd)
# ============================================================
print("=" * 55)
print("STEP 1: PyTorch basics - Tensors + Autograd")
print("=" * 55)

print("""
  NumPy has "arrays". PyTorch has "tensors".
  They look the same, but tensors can:
    1. Run on GPU (1000x faster)
    2. Track gradients AUTOMATICALLY
""")

a_np = np.array([1.0, 2.0, 3.0])
a_pt = torch.tensor([1.0, 2.0, 3.0])

print(f"  NumPy array:    {a_np}")
print(f"  PyTorch tensor: {a_pt}")

# Autograd demo
x = torch.tensor([3.0], requires_grad=True)
y = x ** 2
y.backward()
print(f"""
  THE MAGIC - automatic gradients:
    x = 3.0,  y = x^2 = 9.0
    dy/dx = 2*x = 6.0
    PyTorch computed: x.grad = {x.grad[0]:.1f}  (correct!)

  In Labs 01-04 we wrote gradients BY HAND.
  PyTorch does it automatically. For ANY formula.
""")

input("  Press Enter to continue...")


# ============================================================
# STEP 2: PREPARE THE DATA
# ============================================================
print("\n" + "=" * 55)
print("STEP 2: Same data, now as PyTorch tensors")
print("=" * 55)

X_raw = np.array([
    [22, 25, 0.5], [25, 30, 0.3], [30, 35, 1.0], [35, 40, 0.5],
    [28, 45, 2.0], [45, 50, 0.2], [32, 55, 3.0], [40, 60, 2.5],
    [35, 65, 1.5], [28, 70, 4.0], [50, 55, 3.5], [38, 75, 2.0],
    [42, 80, 1.0], [33, 85, 3.5], [29, 90, 4.5], [45, 95, 2.0],
])
y_raw = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

X_min, X_max = X_raw.min(0), X_raw.max(0)
X_norm = (X_raw - X_min) / (X_max - X_min)

X = torch.tensor(X_norm, dtype=torch.float32).to(device)
y = torch.tensor(y_raw, dtype=torch.float32).reshape(-1, 1).to(device)

print(f"""
  X shape: {X.shape}   (16 customers, 3 features)
  y shape: {y.shape}  (16 labels)
""")

input("  Press Enter to build the model...")


# ============================================================
# STEP 3: BUILD THE MODEL
# ============================================================
print("\n" + "=" * 55)
print("STEP 3: Build the model")
print("=" * 55)

print("""
  Lab 04 (NumPy): 4 weight arrays + 15 lines of gradient math
  PyTorch:        just DESCRIBE what you want:
""")

model = nn.Sequential(
    nn.Linear(3, 4),
    nn.Sigmoid(),
    nn.Linear(4, 1),
    nn.Sigmoid(),
).to(device)

print(f"  model = nn.Sequential(")
print(f"      nn.Linear(3, 4),   # input -> hidden  (auto-creates W, b)")
print(f"      nn.Sigmoid(),      # activation")
print(f"      nn.Linear(4, 1),   # hidden -> output")
print(f"      nn.Sigmoid(),      # output probability")
print(f"  )")

total_params = sum(p.numel() for p in model.parameters())
print(f"\n  Total: {total_params} learnable parameters (same 21 as Lab 04)")

input("\n  Press Enter to see loss + optimizer...")


# ============================================================
# STEP 4: LOSS FUNCTION + OPTIMIZER
# ============================================================
print("\n" + "=" * 55)
print("STEP 4: Loss function and optimizer")
print("=" * 55)

loss_fn = nn.BCELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=2.0)

print(f"""
  loss_fn   = nn.BCELoss()           # same loss, one line
  optimizer = torch.optim.SGD(...)   # handles weight updates

  No manual gradient math needed!
""")

input("  Press Enter to train...")


# ============================================================
# STEP 5: TRAINING LOOP (just 4 lines!)
# ============================================================
print("\n" + "=" * 55)
print("STEP 5: Training")
print("=" * 55)

print("""
  The training loop is just 4 lines:
    pred = model(X)              # forward pass
    loss = loss_fn(pred, y)      # compute loss
    loss.backward()              # compute ALL gradients
    optimizer.step()             # update ALL weights
""")

torch.manual_seed(42)
model = nn.Sequential(
    nn.Linear(3, 4), nn.Sigmoid(),
    nn.Linear(4, 1), nn.Sigmoid(),
).to(device)
loss_fn = nn.BCELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=2.0)

print(f"  {'Round':>6} | {'Loss':>8} | {'Accuracy':>9}")
print(f"  {'-'*35}")

for epoch in range(2001):
    pred = model(X)
    loss = loss_fn(pred, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    with torch.no_grad():
        predicted = (pred >= 0.5).float()
        correct = (predicted == y).sum().item()
        accuracy = correct / len(y) * 100

    if epoch % 250 == 0 or epoch == 2000:
        print(f"  {epoch:>6} | {loss.item():>8.4f} | {accuracy:>8.1f}%")

input("\n  Press Enter to test on new customers...")


# ============================================================
# STEP 6: PREDICT NEW CUSTOMERS
# ============================================================
print(f"\n{'='*55}")
print("STEP 6: Predict new customers")
print("=" * 55)

new_raw = np.array([
    [24, 28, 0.5], [35, 50, 1.0], [30, 70, 3.0], [50, 40, 0.3],
    [28, 85, 4.0], [40, 60, 2.0], [55, 30, 0.2], [33, 95, 5.0],
])
new_norm = (new_raw - X_min) / (X_max - X_min)
X_new = torch.tensor(new_norm, dtype=torch.float32).to(device)

with torch.no_grad():
    predictions = model(X_new)

print(f"\n  {'Age':>5} {'Salary':>7} {'Hours':>6} {'Prob':>8} {'Buy?':>6}")
print(f"  {'-'*38}")
for i in range(len(new_raw)):
    age, sal, hrs = new_raw[i]
    prob = predictions[i].item()
    buy = "YES" if prob >= 0.5 else "NO"
    bar = "#" * int(prob * 20)
    print(f"  {age:>5.0f} {sal:>6.0f}k {hrs:>5.1f} {prob:>7.0%} {buy:>6}  {bar}")

input("\n  Press Enter to see the code comparison...")


# ============================================================
# STEP 7: SIDE BY SIDE - NumPy vs PyTorch
# ============================================================
print(f"\n{'='*55}")
print("STEP 7: NumPy (Lab 04) vs PyTorch (Lab 05)")
print("=" * 55)

print("""
  NumPy (Lab 04) - 20 lines:           PyTorch (Lab 05) - 8 lines:
  +---------------------------------+   +----------------------------------+
  | W1 = np.random.randn(3,4)*0.5  |   | model = nn.Sequential(           |
  | b1 = np.zeros(4)               |   |     nn.Linear(3,4), nn.Sigmoid(),|
  | W2 = np.random.randn(4,1)*0.5  |   |     nn.Linear(4,1), nn.Sigmoid(),|
  | b2 = np.zeros(1)               |   | )                                |
  | z1 = X @ W1 + b1               |   | loss_fn = nn.BCELoss()           |
  | a1 = sigmoid(z1)               |   | optimizer = SGD(model.params())  |
  | z2 = a1 @ W2 + b2              |   |                                  |
  | pred = sigmoid(z2)             |   | pred = model(X)                  |
  | d2 = pred - y                  |   | loss = loss_fn(pred, y)          |
  | gW2 = a1.T @ d2 / n            |   | loss.backward()    # auto!      |
  | ... (6 more lines)             |   | optimizer.step()   # auto!      |
  +---------------------------------+   +----------------------------------+

  Same result. PyTorch automates the hard parts.

  SGD vs Adam:
    SGD:  fixed step size (simple, predictable)
    Adam: adapts step size per-weight (usually better, less tuning)
""")


# ============================================================
# SUMMARY
# ============================================================
print(f"{'='*55}")
print("SUMMARY - What you learned in Lab 05:")
print(f"{'='*55}")

print("""
  1. TENSORS = arrays that track gradients
     torch.tensor() is like np.array() but with autograd.

  2. nn.Sequential = stack layers easily
     PyTorch creates all weights/biases automatically.

  3. AUTOGRAD = no manual gradient math!
     loss.backward() computes ALL gradients for you.

  4. OPTIMIZERS do the weight updates
     SGD:  simple, fixed learning rate
     Adam: smart, adapts per-weight (usually better)

  THE JOURNEY SO FAR:
    Lab 01: score = x*w + b                (1 neuron)
    Lab 03: hidden layer, backprop by hand  (3 neurons)
    Lab 04: X @ W + b with NumPy            (matrix math)
    Lab 05: model(X) with PyTorch           (real framework)

  Next: MNIST - teaching a network to see real images.
  (60,000 handwritten digits - the "Hello World" of AI)
""")
