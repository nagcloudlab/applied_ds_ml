"""
02 - Activation Functions

In 01, we used Sigmoid to squish numbers into 0-1.
But there are other activation functions, each with
a different shape and purpose.

This is the toolbox every neural network picks from.
"""

import numpy as np
import matplotlib.pyplot as plt


# --- Activation definitions ---
def relu(x):
    return np.maximum(0, x)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

def softmax(x):
    exp_x = np.exp(x - np.max(x))
    return exp_x / exp_x.sum()


# ============================================================
# STEP 1: ReLU -- the workhorse
# ============================================================
print("=" * 55)
print("STEP 1: ReLU -- the most popular activation")
print("=" * 55)

print("""
  ReLU(x) = max(0, x)

  Negative input -> 0     (neuron is OFF)
  Positive input -> stays  (neuron is ON)

  Examples:
    ReLU(-5)  = 0
    ReLU(0)   = 0
    ReLU(3.7) = 3.7

  Simple, fast, and used in almost every hidden layer.
""")

input("  Press Enter to see Sigmoid and Tanh...")


# ============================================================
# STEP 2: Sigmoid and Tanh
# ============================================================
print(f"\n{'='*55}")
print("STEP 2: Sigmoid and Tanh")
print("=" * 55)

print("""
  Sigmoid: squishes to (0, 1)
    Used for binary output: "Pass or Fail?"
    sigmoid(-10) = 0.00, sigmoid(0) = 0.50, sigmoid(10) = 1.00

  Tanh: squishes to (-1, +1)
    Like sigmoid but centered at 0
    Used in some sequence models (RNN)
    tanh(-10) = -1.00, tanh(0) = 0.00, tanh(10) = 1.00
""")

input("  Press Enter to see all three plotted...")


# ============================================================
# STEP 3: Plot ReLU, Sigmoid, Tanh
# ============================================================
print(f"\n{'='*55}")
print("STEP 3: Visual comparison")
print("=" * 55)

x = np.linspace(-5, 5, 300)

fig, axes = plt.subplots(1, 3, figsize=(14, 4))

axes[0].plot(x, relu(x), color="blue")
axes[0].set_title("ReLU: max(0, x)")
axes[0].axhline(0, color="gray", linewidth=0.5)
axes[0].axvline(0, color="gray", linewidth=0.5)

axes[1].plot(x, sigmoid(x), color="green")
axes[1].set_title("Sigmoid: 1 / (1 + e^-x)")
axes[1].axhline(0.5, color="gray", linestyle="--", linewidth=0.5)

axes[2].plot(x, tanh(x), color="red")
axes[2].set_title("Tanh: (e^x - e^-x) / (e^x + e^-x)")
axes[2].axhline(0, color="gray", linewidth=0.5)

for ax in axes:
    ax.set_xlabel("x")
    ax.set_ylabel("output")
    ax.grid(alpha=0.3)

plt.tight_layout()
plt.show()

input("  Press Enter for Softmax...")


# ============================================================
# STEP 4: Softmax -- for multi-class
# ============================================================
print(f"\n{'='*55}")
print("STEP 4: Softmax -- when there are many classes")
print("=" * 55)

logits = np.array([2.0, 1.0, 0.5])
probs = softmax(logits)

print(f"""
  Softmax converts raw scores into probabilities that sum to 1.
  Used when the answer is one of MANY classes (not just yes/no).

  Example: is this a Cat, Dog, or Horse?

  Raw scores (logits): {logits.tolist()}
  Softmax probabilities: {np.round(probs, 4).tolist()}
  Sum: {round(probs.sum(), 4)}

  Highest: class {np.argmax(probs)} ({probs[np.argmax(probs)]:.0%})
""")


# ============================================================
# SUMMARY
# ============================================================
print(f"""
{'='*55}
SUMMARY
{'='*55}

  Activation   Output range   Used for
  ---------    ------------   --------
  ReLU         [0, inf)       Hidden layers (default choice)
  Sigmoid      (0, 1)         Binary output (Pass/Fail)
  Tanh         (-1, 1)        Some sequence models
  Softmax      (0,1) sum=1    Multi-class output (Cat/Dog/Horse)

  Without activation, layers collapse into one linear model.
  Activation adds the CURVES that let networks learn complex patterns.

  Next: the neuron has activations, but who picks the weights?
  Let the neuron learn them by itself.
""")
