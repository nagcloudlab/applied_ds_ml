"""
LAB 08: CNN - How Computers Actually See
=========================================
Lab 06: Flatten image -> feed 784 pixels -> ~97%
Lab 08: Use CONVOLUTION to detect patterns  -> 99%+

THE PROBLEM WITH FLATTENING:
  We flattened the 28x28 image into 784 numbers.
  The network lost all SPATIAL information.
  It doesn't know pixel 5 is NEXT TO pixel 6.

WHAT CNN DOES DIFFERENTLY:
  Instead of looking at ALL pixels at once,
  it slides a small WINDOW across the image,
  detecting patterns like edges, curves, corners.
"""

import torch
import torch.nn as nn
from torchvision import datasets, transforms

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# ============================================================
# STEP 1: WHY CNN? (The problem with flattening)
# ============================================================
print("=" * 55)
print("STEP 1: Why CNN? The problem with flattening")
print("=" * 55)

print("""
  Lab 06 (Flatten approach):
    . . # # . .       [., ., #, #, ., ., ., #, #, #, ...]
    . # # # . .    ->  (784 random-order numbers)
    . . # . . .        Lost! We don't know # is NEXT to #.

  CNN approach: slide a small 3x3 window across the image.
  Each position gives a score. High score = "pattern found here!"

  This creates a "feature map" showing WHERE patterns are.
""")

input("  Press Enter to see how a filter works...")


# ============================================================
# STEP 2: HOW A FILTER WORKS (with real numbers)
# ============================================================
print("\n" + "=" * 55)
print("STEP 2: How a 3x3 filter detects edges")
print("=" * 55)

print("""
  A filter is a small grid of weights. Let's trace one:

  Vertical edge filter:     Image patch (edge):
    [-1  0  1]                [0  0  1]
    [-1  0  1]                [0  0  1]
    [-1  0  1]                [0  0  1]

  Convolution = multiply matching positions, then sum:
    (-1*0) + (0*0) + (1*1) +
    (-1*0) + (0*0) + (1*1) +
    (-1*0) + (0*0) + (1*1) = 3  (HIGH! Edge found!)

  Now a flat patch (no edge):
    [1  1  1]
    [1  1  1]     -> (-1+0+1) + (-1+0+1) + (-1+0+1) = 0
    [1  1  1]        (LOW! No edge here.)

  A CNN learns MANY filters automatically:
    Filter 1: vertical edges    Filter 3: curves
    Filter 2: horizontal edges  Filter 4: corners ...
""")

input("  Press Enter to see the CNN architecture...")


# ============================================================
# STEP 3: CNN ARCHITECTURE
# ============================================================
print("\n" + "=" * 55)
print("STEP 3: Building the CNN")
print("=" * 55)

print("""
  3 types of layers:

  1. CONV: slide filters to detect patterns
  2. POOLING: shrink the image (keep strongest signals)
     [1 3]
     [2 4] -> max = 4  (keeps only the MAX in each 2x2 block)
  3. FULLY CONNECTED: classify the detected patterns

  Pipeline:
    28x28 image
      -> Conv1 (16 filters) -> Pool -> 14x14
      -> Conv2 (32 filters) -> Pool -> 7x7
      -> Flatten (32*7*7 = 1568)
      -> Linear -> 10 digit classes
""")

class CNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 16, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.relu = nn.ReLU()
        self.fc1 = nn.Linear(32 * 7 * 7, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.pool(self.relu(self.conv1(x)))   # 1x28x28 -> 16x14x14
        x = self.pool(self.relu(self.conv2(x)))   # 16x14x14 -> 32x7x7
        x = x.view(-1, 32 * 7 * 7)                # flatten
        x = self.relu(self.fc1(x))                 # 1568 -> 128
        x = self.fc2(x)                            # 128 -> 10
        return x

model = CNN().to(device)
total_params = sum(p.numel() for p in model.parameters())

print(f"  Layer-by-layer:")
print(f"    Conv1:  1 -> 16 filters (3x3) = {sum(p.numel() for p in model.conv1.parameters()):>6} params")
print(f"    Conv2: 16 -> 32 filters (3x3) = {sum(p.numel() for p in model.conv2.parameters()):>6} params")
print(f"    FC1:   1568 -> 128             = {sum(p.numel() for p in model.fc1.parameters()):>6} params")
print(f"    FC2:   128 -> 10               = {sum(p.numel() for p in model.fc2.parameters()):>6} params")
print(f"    Total: {total_params:,}")

input("\n  Press Enter to see data flow through the CNN...")


# ============================================================
# STEP 4: TRACE DATA THROUGH THE CNN
# ============================================================
print("\n" + "=" * 55)
print("STEP 4: Watch data flow through the CNN")
print("=" * 55)

transform = transforms.ToTensor()
train_data = datasets.MNIST('data', train=True, download=True, transform=transform)
test_data = datasets.MNIST('data', train=False, download=True, transform=transform)

sample_image = train_data[0][0].unsqueeze(0).to(device)

print(f"\n  Input: digit '{train_data[0][1]}', shape {list(sample_image.shape)}")
print(f"         [batch=1, channels=1, height=28, width=28]")

with torch.no_grad():
    x = sample_image
    x = model.conv1(x)
    print(f"\n  After Conv1:  {list(x.shape)}  (16 filters, each 28x28)")
    x = model.relu(x)
    x = model.pool(x)
    print(f"  After Pool1:  {list(x.shape)}  (shrunk to 14x14)")
    x = model.conv2(x)
    print(f"  After Conv2:  {list(x.shape)}  (32 filters, each 14x14)")
    x = model.relu(x)
    x = model.pool(x)
    print(f"  After Pool2:  {list(x.shape)}  (shrunk to 7x7)")
    x = x.view(-1, 32 * 7 * 7)
    print(f"  After Flatten: {list(x.shape)} (32*7*7 = 1568 numbers)")
    x = model.relu(model.fc1(x))
    print(f"  After FC1:    {list(x.shape)}  (128 neurons)")
    x = model.fc2(x)
    print(f"  After FC2:    {list(x.shape)}   (10 digit scores)")

input("\n  Press Enter to train...")


# ============================================================
# STEP 5: TRAIN THE CNN
# ============================================================
print("\n" + "=" * 55)
print("STEP 5: Training the CNN")
print("=" * 55)

train_loader = torch.utils.data.DataLoader(train_data, batch_size=64, shuffle=True)
test_loader = torch.utils.data.DataLoader(test_data, batch_size=1000)

model = CNN().to(device)
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

print(f"""
  Same training loop as Lab 06, only the model changed!
  Training for 5 epochs...
""")

for epoch in range(5):
    model.train()
    total_loss = correct = total = 0

    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        outputs = model(images)
        loss = loss_fn(outputs, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()
        correct += (outputs.argmax(1) == labels).sum().item()
        total += labels.size(0)

    train_acc = correct / total * 100

    model.eval()
    test_correct = test_total = 0
    with torch.no_grad():
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            test_correct += (outputs.argmax(1) == labels).sum().item()
            test_total += labels.size(0)
    test_acc = test_correct / test_total * 100

    print(f"  Epoch {epoch+1}/5 | Loss: {total_loss/len(train_loader):.4f} | Train: {train_acc:.1f}% | Test: {test_acc:.1f}%")

print(f"""
  Lab 06 (Flatten + Linear): ~97% test accuracy
  Lab 08 (CNN):              ~{test_acc:.1f}% test accuracy

  CNN wins because it understands SPATIAL patterns!
""")

input("  Press Enter to see predictions...")


# ============================================================
# STEP 6: PREDICTIONS
# ============================================================
print(f"\n{'='*55}")
print("STEP 6: Predictions on test images")
print("=" * 55)

model.eval()
test_images, test_labels = next(iter(test_loader))
test_images, test_labels = test_images.to(device), test_labels.to(device)

with torch.no_grad():
    outputs = model(test_images[:15])
    predictions = outputs.argmax(dim=1)
    confidences = torch.softmax(outputs, dim=1)

wrong_count = 0
print(f"\n  15 test images:\n")
for i in range(15):
    image = test_images[i].squeeze().cpu()
    actual = test_labels[i].item()
    pred = predictions[i].item()
    conf = confidences[i][pred].item()
    status = "OK" if pred == actual else "WRONG"
    if pred != actual:
        wrong_count += 1

    mini = ""
    for r in range(0, 28, 4):
        for c in range(0, 28, 4):
            val = image[r, c].item()
            mini += "##" if val > 0.3 else "  "
        mini += " | "

    print(f"  {mini} Actual={actual} Pred={pred} ({conf:.0%}) {status}")

print(f"\n  {15-wrong_count}/15 correct!")


# ============================================================
# SUMMARY
# ============================================================
print(f"\n{'='*55}")
print("SUMMARY - What you learned in Lab 08:")
print(f"{'='*55}")

print(f"""
  1. CONVOLUTION = sliding a small filter across an image
     3x3 filter detects local patterns (edges, curves).

  2. FILTERS are learned, not hand-designed
     The network discovers what to look for automatically.

  3. POOLING shrinks the image (keeps strongest signals)
     28x28 -> 14x14 -> 7x7

  4. CNN > Linear for images because:
     - Understands spatial neighbors
     - Same filter works everywhere (parameter sharing)
     - Builds: edges -> shapes -> objects (hierarchy)

  5. Architecture: Conv -> ReLU -> Pool -> Conv -> ReLU -> Pool -> FC

  Lab 06 (Linear): ~97% | Lab 08 (CNN): ~{test_acc:.0f}%

  Next: Cat vs Dog - transfer learning with real photos.
  Use a pretrained network instead of training from scratch!
""")
