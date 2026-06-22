"""
LAB 06: TEACH A NETWORK TO SEE (MNIST Handwritten Digits)
==========================================================
Lab 01-05: tiny data, 16 samples, 3 features
Lab 06:    REAL images, 60,000 samples, 784 pixels each!

THE PROBLEM:
  Given a 28x28 pixel handwritten digit image,
  predict which digit it is (0-9).

  This is the "Hello World" of AI / deep learning.

WHAT'S NEW:
  1. Real dataset (MNIST - 70,000 images)
  2. Image data (pixels as inputs)
  3. Multi-class (10 digits, not just yes/no)
  4. DataLoaders (process data in batches)
  5. Training/Test split (measure real performance)
"""

import torch
import torch.nn as nn
from torchvision import datasets, transforms

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"  Using device: {device}")

# ============================================================
# STEP 1: WHAT DOES THE DATA LOOK LIKE?
# ============================================================
print("=" * 55)
print("STEP 1: Loading MNIST (handwritten digits)")
print("=" * 55)

print("""
  MNIST = 70,000 images of handwritten digits (0-9)
    - 60,000 for training
    - 10,000 for testing (never seen during training)

  Each image is 28x28 pixels = 784 numbers.
  Each pixel is 0 (white) to 1 (black).

  Downloading...
""")

transform = transforms.ToTensor()
train_data = datasets.MNIST('data', train=True, download=True, transform=transform)
test_data = datasets.MNIST('data', train=False, download=True, transform=transform)

print(f"  Training images: {len(train_data)}")
print(f"  Testing images:  {len(test_data)}")

# Show a digit as ASCII art
image, label = train_data[0]
pixels = image.squeeze()

print(f"\n  First image is the digit: {label}")
print(f"  Let's see it as ASCII art:\n")

for row in range(28):
    line = "    "
    for col in range(28):
        val = pixels[row, col].item()
        if val > 0.7:
            line += "##"
        elif val > 0.3:
            line += ".."
        else:
            line += "  "
    print(line)

print(f"\n  That's a '{label}'! The network will learn to recognize these.")

input("\n  Press Enter to continue...")


# ============================================================
# STEP 2: HOW IMAGES BECOME INPUTS
# ============================================================
print("\n" + "=" * 55)
print("STEP 2: Image -> numbers -> network")
print("=" * 55)

print(f"""
  A 28x28 image = 784 numbers.
  We FLATTEN it into one long row:

    28x28 grid  ->  [0.0, 0.0, 0.1, ..., 0.9, 0.3, 0.0]
                    (784 numbers in a row)

  So our network input is 784 numbers (one per pixel).
""")

input("  Press Enter to build the model...")


# ============================================================
# STEP 3: BUILD THE MODEL
# ============================================================
print("\n" + "=" * 55)
print("STEP 3: Build the model")
print("=" * 55)

print("""
  Lab 05: 3 inputs  -> 4 hidden -> 1 output  (21 params)
  Lab 06: 784 inputs -> 128 -> 64 -> 10 outputs (101,770 params!)

  Why 10 outputs? One per digit: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  Highest score = the network's answer.
""")

model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(784, 128),
    nn.ReLU(),
    nn.Linear(128, 64),
    nn.ReLU(),
    nn.Linear(64, 10),
).to(device)

total_params = sum(p.numel() for p in model.parameters())
print(f"  Total parameters: {total_params:,}")

print(f"""
  NEW:
  - nn.Flatten() reshapes 28x28 -> 784
  - No Sigmoid at end: CrossEntropyLoss handles multi-class
  - TWO hidden layers (128 + 64 neurons)
""")

input("  Press Enter to set up training...")


# ============================================================
# STEP 4: DATALOADER + LOSS + OPTIMIZER
# ============================================================
print("\n" + "=" * 55)
print("STEP 4: DataLoader, Loss, Optimizer")
print("=" * 55)

print("""
  NEW CONCEPT: DataLoader (batches)

  Lab 05: fed ALL 16 customers at once.
  Lab 06: 60,000 images! Can't do that.

  Solution: process 64 images at a time (a "batch").
    Batch 1: images 0-63    -> update weights
    Batch 2: images 64-127  -> update weights
    ...
    = 1 EPOCH (one pass through all data)

  Why batches?
    - Fits in memory
    - Update weights more often -> faster learning
""")

train_loader = torch.utils.data.DataLoader(
    train_data, batch_size=64, shuffle=True
)
test_loader = torch.utils.data.DataLoader(
    test_data, batch_size=1000
)

loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

print(f"  DataLoader: {len(train_loader)} batches of 64 images")
print(f"  Loss: CrossEntropyLoss (for 10 classes)")
print(f"  Optimizer: Adam (lr=0.001)")

input("\n  Press Enter to train (this takes ~30 seconds)...")


# ============================================================
# STEP 5: TRAINING
# ============================================================
print("\n" + "=" * 55)
print("STEP 5: Training on 60,000 images")
print("=" * 55)

print(f"\n  Training for 5 epochs...\n")

for epoch in range(5):
    model.train()
    total_loss = 0
    correct = 0
    total = 0

    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        outputs = model(images)
        loss = loss_fn(outputs, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()
        predicted = outputs.argmax(dim=1)
        correct += (predicted == labels).sum().item()
        total += labels.size(0)

    train_acc = correct / total * 100
    avg_loss = total_loss / len(train_loader)

    model.eval()
    test_correct = 0
    test_total = 0
    with torch.no_grad():
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            predicted = outputs.argmax(dim=1)
            test_correct += (predicted == labels).sum().item()
            test_total += labels.size(0)
    test_acc = test_correct / test_total * 100

    print(f"  Epoch {epoch+1}/5 | Loss: {avg_loss:.4f} | Train: {train_acc:.1f}% | Test: {test_acc:.1f}%")

print(f"""
  Train accuracy: how well it does on images it SAW
  Test accuracy:  how well it does on images it NEVER saw
""")

input("  Press Enter to see predictions...")


# ============================================================
# STEP 6: SEE THE PREDICTIONS
# ============================================================
print(f"\n{'='*55}")
print("STEP 6: Predictions on test images")
print("=" * 55)

model.eval()
test_images, test_labels = next(iter(test_loader))
test_images, test_labels = test_images.to(device), test_labels.to(device)

with torch.no_grad():
    outputs = model(test_images[:10])
    predictions = outputs.argmax(dim=1)
    confidences = torch.softmax(outputs, dim=1)

print(f"\n  10 test images the network has NEVER seen:\n")

for i in range(10):
    image = test_images[i].squeeze().cpu()
    actual = test_labels[i].item()
    pred = predictions[i].item()
    conf = confidences[i][pred].item()
    status = "OK" if pred == actual else "WRONG!"

    mini = ""
    for r in range(0, 28, 4):
        for c in range(0, 28, 4):
            val = image[r, c].item()
            mini += "##" if val > 0.3 else "  "
        mini += " | "

    print(f"  Image {i+1}: {mini} Actual={actual}, Predicted={pred} ({conf:.0%}) {status}")

input("\n  Press Enter to see per-digit accuracy...")


# ============================================================
# STEP 7: PER-DIGIT ACCURACY
# ============================================================
print(f"\n{'='*55}")
print("STEP 7: How well does it recognize each digit?")
print("=" * 55)

digit_correct = [0] * 10
digit_total = [0] * 10

model.eval()
with torch.no_grad():
    for images, labels in test_loader:
        images, labels = images.to(device), labels.to(device)
        outputs = model(images)
        preds = outputs.argmax(dim=1)
        for i in range(len(labels)):
            digit = labels[i].item()
            digit_total[digit] += 1
            if preds[i].item() == digit:
                digit_correct[digit] += 1

print(f"\n  {'Digit':>6} | {'Correct':>8} | {'Total':>6} | {'Accuracy':>9} | Visual")
print(f"  {'-'*55}")

for d in range(10):
    acc = digit_correct[d] / digit_total[d] * 100
    bar = "#" * int(acc / 5)
    print(f"  {d:>6} | {digit_correct[d]:>8} | {digit_total[d]:>6} | {acc:>8.1f}% | {bar}")

overall = sum(digit_correct) / sum(digit_total) * 100
print(f"\n  Overall: {overall:.1f}% on 10,000 test images!")


# ============================================================
# SUMMARY
# ============================================================
print(f"\n{'='*55}")
print("SUMMARY - What you learned in Lab 06:")
print(f"{'='*55}")

print(f"""
  1. IMAGES = just numbers
     28x28 pixels = 784 numbers. Flatten and feed to network.

  2. MULTI-CLASS output
     10 outputs (one per digit), highest score wins.
     CrossEntropyLoss handles this automatically.

  3. BATCHES and DataLoaders
     Process 64 images at a time instead of all 60,000.

  4. TRAIN vs TEST split
     Train on 60,000, test on 10,000 UNSEEN images.

  5. DEEPER networks work better
     784 -> 128 -> 64 -> 10 (three layers!)

  Result: ~{overall:.0f}% accuracy on handwritten digits!

  Next: Overfitting - when your network memorizes
  instead of learning. And how to fix it.
""")
