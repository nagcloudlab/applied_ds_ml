"""
LAB 07: OVERFITTING - When Your Network Memorizes Instead of Learning
=====================================================================
Lab 06: trained on MNIST, got ~97% test accuracy. Great!
Lab 07: what happens when things go WRONG?

THE PROBLEM:
  Imagine a student who memorizes every exam answer word-for-word.
  They get 100% on practice tests (seen before).
  But on a NEW exam? They fail.

  Neural networks do the SAME thing. It's called OVERFITTING.
  The network memorizes training data instead of learning patterns.

WHAT YOU'LL LEARN:
  1. How to CREATE overfitting (so you can recognize it)
  2. Fix 1: Dropout (randomly disable neurons during training)
  3. Fix 2: Early Stopping (stop before it memorizes)
"""

import torch
import torch.nn as nn
from torchvision import datasets, transforms

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# ============================================================
# STEP 1: SET UP THE EXPERIMENT
# ============================================================
print("=" * 55)
print("STEP 1: Creating an overfitting scenario")
print("=" * 55)

print("""
  To see overfitting clearly, we need:
    1. A SMALL dataset (easy to memorize)
    2. A BIG network (too many parameters for the data)

  We'll use only 1,000 MNIST images (instead of 60,000)
  with a large network (way more capacity than needed).
""")

transform = transforms.ToTensor()
full_train = datasets.MNIST('data', train=True, download=True, transform=transform)
test_data = datasets.MNIST('data', train=False, download=True, transform=transform)

# Use only 1000 training images (to make overfitting easy)
small_train = torch.utils.data.Subset(full_train, range(1000))

train_loader = torch.utils.data.DataLoader(small_train, batch_size=64, shuffle=True)
test_loader = torch.utils.data.DataLoader(test_data, batch_size=1000)

print(f"  Training images: {len(small_train)} (only!)")
print(f"  Test images:     {len(test_data)}")

input("\n  Press Enter to train an oversized network...")


# ============================================================
# STEP 2: OVERFIT! (no regularization)
# ============================================================
print("\n" + "=" * 55)
print("STEP 2: Training without protection (will overfit!)")
print("=" * 55)

print("""
  Network: 784 -> 256 -> 128 -> 10
  That's 235,146 parameters for only 1,000 images!
  Way too powerful. It will MEMORIZE instead of LEARN.
""")

model_overfit = nn.Sequential(
    nn.Flatten(),
    nn.Linear(784, 256),
    nn.ReLU(),
    nn.Linear(256, 128),
    nn.ReLU(),
    nn.Linear(128, 10),
).to(device)

loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model_overfit.parameters(), lr=0.001)


def evaluate(model, loader):
    model.eval()
    correct = total = 0
    with torch.no_grad():
        for images, labels in loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            correct += (outputs.argmax(1) == labels).sum().item()
            total += labels.size(0)
    return correct / total * 100


print(f"\n  {'Epoch':>6} | {'Train Acc':>10} | {'Test Acc':>10} | Gap")
print(f"  {'-'*50}")

overfit_history = []

for epoch in range(1, 21):
    model_overfit.train()
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        outputs = model_overfit(images)
        loss = loss_fn(outputs, labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    train_acc = evaluate(model_overfit, train_loader)
    test_acc = evaluate(model_overfit, test_loader)
    gap = train_acc - test_acc
    overfit_history.append((epoch, train_acc, test_acc))

    if epoch % 2 == 0 or epoch == 1:
        flag = " <-- OVERFITTING!" if gap > 10 else ""
        print(f"  {epoch:>6} | {train_acc:>9.1f}% | {test_acc:>9.1f}% | {gap:>+5.1f}%{flag}")

print(f"""
  See the gap? Train ~{overfit_history[-1][1]:.0f}% but Test ~{overfit_history[-1][2]:.0f}%.
  The network MEMORIZED the 1000 training images
  but can't generalize to new images.
""")

input("  Press Enter to see Fix 1: Dropout...")


# ============================================================
# STEP 3: FIX 1 - DROPOUT
# ============================================================
print("\n" + "=" * 55)
print("STEP 3: Fix 1 - Dropout")
print("=" * 55)

print("""
  DROPOUT: during training, randomly turn OFF 50% of neurons.

  Why it works:
    - Forces the network to NOT rely on any single neuron
    - Like studying with different friends each day
    - Each "sub-network" learns independently
    - At test time, all neurons are active (averaged)

  Just add nn.Dropout(0.5) after each hidden layer!
""")

model_dropout = nn.Sequential(
    nn.Flatten(),
    nn.Linear(784, 256),
    nn.ReLU(),
    nn.Dropout(0.5),        # randomly turn off 50% of neurons
    nn.Linear(256, 128),
    nn.ReLU(),
    nn.Dropout(0.5),        # again!
    nn.Linear(128, 10),
).to(device)

optimizer2 = torch.optim.Adam(model_dropout.parameters(), lr=0.001)

print(f"\n  {'Epoch':>6} | {'Train Acc':>10} | {'Test Acc':>10} | Gap")
print(f"  {'-'*50}")

dropout_history = []

for epoch in range(1, 21):
    model_dropout.train()
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        outputs = model_dropout(images)
        loss = loss_fn(outputs, labels)
        optimizer2.zero_grad()
        loss.backward()
        optimizer2.step()

    train_acc = evaluate(model_dropout, train_loader)
    test_acc = evaluate(model_dropout, test_loader)
    gap = train_acc - test_acc
    dropout_history.append((epoch, train_acc, test_acc))

    if epoch % 2 == 0 or epoch == 1:
        print(f"  {epoch:>6} | {train_acc:>9.1f}% | {test_acc:>9.1f}% | {gap:>+5.1f}%")

print(f"""
  Much smaller gap! Dropout prevents memorization.
  Train accuracy is lower (harder to memorize with dropout)
  but Test accuracy is BETTER (generalizes more).
""")

input("  Press Enter to see Fix 2: Early Stopping...")


# ============================================================
# STEP 4: FIX 2 - EARLY STOPPING
# ============================================================
print("\n" + "=" * 55)
print("STEP 4: Fix 2 - Early Stopping")
print("=" * 55)

print("""
  EARLY STOPPING: stop training when test loss stops improving.

  Why? At first, both train and test improve together.
  Then test loss starts RISING while train loss keeps dropping.
  That's the moment to STOP - the network just started memorizing.

  It's like studying: after a point, more studying = burnout.
""")

model_early = nn.Sequential(
    nn.Flatten(),
    nn.Linear(784, 256),
    nn.ReLU(),
    nn.Linear(256, 128),
    nn.ReLU(),
    nn.Linear(128, 10),
).to(device)

optimizer3 = torch.optim.Adam(model_early.parameters(), lr=0.001)

print(f"\n  {'Epoch':>6} | {'Train Loss':>11} | {'Test Loss':>10} | {'Test Acc':>9} | Status")
print(f"  {'-'*65}")

best_test_loss = float('inf')
patience = 3
wait = 0
best_epoch = 0

for epoch in range(1, 31):
    # Train
    model_early.train()
    train_loss_sum = 0
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        outputs = model_early(images)
        loss = loss_fn(outputs, labels)
        optimizer3.zero_grad()
        loss.backward()
        optimizer3.step()
        train_loss_sum += loss.item()
    train_loss = train_loss_sum / len(train_loader)

    # Test loss
    model_early.eval()
    test_loss_sum = 0
    test_correct = test_total = 0
    with torch.no_grad():
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model_early(images)
            test_loss_sum += loss_fn(outputs, labels).item()
            test_correct += (outputs.argmax(1) == labels).sum().item()
            test_total += labels.size(0)
    test_loss = test_loss_sum / len(test_loader)
    test_acc = test_correct / test_total * 100

    # Early stopping check
    if test_loss < best_test_loss:
        best_test_loss = test_loss
        best_epoch = epoch
        wait = 0
        status = "improving"
    else:
        wait += 1
        status = f"no improvement ({wait}/{patience})"

    if epoch % 2 == 0 or epoch <= 3 or wait >= patience:
        print(f"  {epoch:>6} | {train_loss:>11.4f} | {test_loss:>10.4f} | {test_acc:>8.1f}% | {status}")

    if wait >= patience:
        print(f"\n  STOPPED at epoch {epoch}! Best was epoch {best_epoch}.")
        print(f"  Test loss stopped improving for {patience} epochs in a row.")
        break

if wait < patience:
    print(f"\n  Finished 30 epochs (no early stop triggered).")

input("\n  Press Enter to see the comparison...")


# ============================================================
# STEP 5: SIDE-BY-SIDE COMPARISON
# ============================================================
print(f"\n{'='*55}")
print("STEP 5: Comparison")
print("=" * 55)

overfit_final = overfit_history[-1]
dropout_final = dropout_history[-1]

print(f"""
  +---------------------+----------+----------+--------+
  |    Method           | Train    | Test     | Gap    |
  +---------------------+----------+----------+--------+
  | No protection       | {overfit_final[1]:>6.1f}%  | {overfit_final[2]:>6.1f}%  | {overfit_final[1]-overfit_final[2]:>+5.1f}% |
  | + Dropout(0.5)      | {dropout_final[1]:>6.1f}%  | {dropout_final[2]:>6.1f}%  | {dropout_final[1]-dropout_final[2]:>+5.1f}% |
  | + Early Stopping    | (stops before memorizing)          |
  +---------------------+----------+----------+--------+

  KEY INSIGHT:
    High train accuracy + low test accuracy = OVERFITTING
    The goal is high TEST accuracy, not high TRAIN accuracy!
""")


# ============================================================
# SUMMARY
# ============================================================
print(f"{'='*55}")
print("SUMMARY - What you learned in Lab 07:")
print(f"{'='*55}")

print("""
  1. OVERFITTING = memorizing instead of learning
     The network aces training data but fails on new data.
     Like a student who memorizes answers, not concepts.

  2. DROPOUT = randomly turn off neurons during training
     Forces the network to learn robust patterns.
     nn.Dropout(0.5) after hidden layers.

  3. EARLY STOPPING = stop when test loss stops improving
     Monitor test loss each epoch. Stop when it rises.
     Prevents the network from "over-studying."

  4. WATCH THE GAP
     Train accuracy vs Test accuracy tells the whole story.
     Small gap = good generalization. Big gap = overfitting.

  Next: CNNs - how computers actually see images.
  Convolutional filters that detect edges, shapes, textures.
""")
