"""
LAB 09: CAT vs DOG - Transfer Learning
========================================
Lab 08: trained a CNN from scratch on MNIST (grayscale, 28x28)
Lab 09: classify REAL photos using a PRETRAINED network!

THE BIG IDEA:
  Training a CNN from scratch needs millions of images.
  But someone already trained ResNet on 1.2 million images
  (ImageNet) - it already knows edges, shapes, textures!

  TRANSFER LEARNING: take that pretrained network,
  replace just the last layer, and fine-tune on YOUR data.
  Like hiring an expert artist and just teaching them
  "these are cats, these are dogs."

DATASET: OxfordIIITPet (auto-downloads ~800MB first run)
"""

import torch
import torch.nn as nn
from torchvision import datasets, transforms, models

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# ============================================================
# STEP 1: LOAD THE DATASET
# ============================================================
print("=" * 55)
print("STEP 1: Loading OxfordIIITPet dataset")
print("=" * 55)

print("""
  OxfordIIITPet: ~7,400 images of 37 cat/dog breeds.
  We'll simplify to just 2 classes: CAT vs DOG.

  Data augmentation (make training data more varied):
    - Resize to 224x224 (ResNet's expected size)
    - RandomHorizontalFlip (mirror some images)
    - Normalize with ImageNet statistics

  Downloading (first run only, ~800MB)...
""")

train_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225]),
])

test_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225]),
])

train_full = datasets.OxfordIIITPet(
    'data', split='trainval', download=True, transform=train_transform
)
test_full = datasets.OxfordIIITPet(
    'data', split='test', download=True, transform=test_transform
)


def is_cat(label):
    """OxfordIIITPet: classes 0-11 are cats, 12-36 are dogs."""
    return 1 if label < 12 else 0


# Create binary labels (1=cat, 0=dog)
train_labels = [is_cat(train_full[i][1]) for i in range(len(train_full))]
test_labels = [is_cat(test_full[i][1]) for i in range(len(test_full))]

n_train_cats = sum(train_labels)
n_train_dogs = len(train_labels) - n_train_cats

print(f"  Training: {len(train_full)} images ({n_train_cats} cats, {n_train_dogs} dogs)")
print(f"  Testing:  {len(test_full)} images")
print(f"  Image size: 3x224x224 (color, resized)")

input("\n  Press Enter to set up transfer learning...")


# ============================================================
# STEP 2: TRANSFER LEARNING SETUP
# ============================================================
print("\n" + "=" * 55)
print("STEP 2: Transfer learning with ResNet18")
print("=" * 55)

print("""
  ResNet18 was trained on ImageNet (1.2 million images, 1000 classes).
  It already knows how to detect:
    - Edges, textures (early layers)
    - Shapes, parts (middle layers)
    - Objects (final layers)

  Our plan:
    1. Load pretrained ResNet18
    2. FREEZE all layers (don't change what it already knows)
    3. Replace the last layer: 1000 classes -> 2 (cat/dog)
    4. Train ONLY the new last layer

  This is like hiring a vision expert and just saying:
  "Use everything you know, but now sort into cat vs dog."
""")

# Load pretrained ResNet18
model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)

# Freeze ALL existing layers
for param in model.parameters():
    param.requires_grad = False

# Replace final layer (originally 1000 classes -> now 2)
model.fc = nn.Linear(model.fc.in_features, 2)

model = model.to(device)

total_params = sum(p.numel() for p in model.parameters())
trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)

print(f"  Total parameters:     {total_params:>10,}")
print(f"  Trainable (new layer): {trainable:>10,}")
print(f"  Frozen (pretrained):  {total_params - trainable:>10,}")
print(f"\n  We're only training {trainable} out of {total_params:,} parameters!")
print(f"  That's {trainable/total_params:.1%} of the network. Fast!")

input("\n  Press Enter to train...")


# ============================================================
# STEP 3: TRAIN
# ============================================================
print("\n" + "=" * 55)
print("STEP 3: Training (only the last layer)")
print("=" * 55)


class CatDogDataset(torch.utils.data.Dataset):
    def __init__(self, base_dataset, binary_labels):
        self.base = base_dataset
        self.labels = binary_labels

    def __len__(self):
        return len(self.base)

    def __getitem__(self, idx):
        image, _ = self.base[idx]
        return image, self.labels[idx]


train_dataset = CatDogDataset(train_full, train_labels)
test_dataset = CatDogDataset(test_full, test_labels)

train_loader = torch.utils.data.DataLoader(
    train_dataset, batch_size=32, shuffle=True, num_workers=0
)
test_loader = torch.utils.data.DataLoader(
    test_dataset, batch_size=32, num_workers=0
)

loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.fc.parameters(), lr=0.001)

print(f"\n  Training for 3 epochs (should be fast!)...\n")

for epoch in range(3):
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

    # Test
    model.eval()
    test_correct = test_total = 0
    with torch.no_grad():
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            test_correct += (outputs.argmax(1) == labels).sum().item()
            test_total += labels.size(0)
    test_acc = test_correct / test_total * 100

    avg_loss = total_loss / len(train_loader)
    print(f"  Epoch {epoch+1}/3 | Loss: {avg_loss:.4f} | Train: {train_acc:.1f}% | Test: {test_acc:.1f}%")

print(f"""
  With just 3 epochs and a frozen backbone, we get ~{test_acc:.0f}%!
""")

input("  Press Enter to see predictions...")


# ============================================================
# STEP 4: PREDICTIONS
# ============================================================
print(f"\n{'='*55}")
print("STEP 4: Sample predictions")
print("=" * 55)

model.eval()
test_iter = iter(test_loader)
sample_images, sample_labels = next(test_iter)
sample_images, sample_labels = sample_images.to(device), sample_labels.to(device)

with torch.no_grad():
    outputs = model(sample_images[:10])
    preds = outputs.argmax(1)
    probs = torch.softmax(outputs, dim=1)

class_names = ["DOG", "CAT"]

print(f"\n  {'#':>3} | {'Actual':>8} | {'Predicted':>10} | {'Confidence':>11} | Status")
print(f"  {'-'*55}")

correct_count = 0
for i in range(10):
    actual = class_names[sample_labels[i].item()]
    predicted = class_names[preds[i].item()]
    conf = probs[i][preds[i]].item()
    ok = "OK" if preds[i].item() == sample_labels[i].item() else "WRONG"
    if ok == "OK":
        correct_count += 1
    print(f"  {i+1:>3} | {actual:>8} | {predicted:>10} | {conf:>10.0%} | {ok}")

print(f"\n  {correct_count}/10 correct on this batch!")

input("\n  Press Enter to see the key comparison...")


# ============================================================
# STEP 5: FROM SCRATCH vs TRANSFER LEARNING
# ============================================================
print(f"\n{'='*55}")
print("STEP 5: Why transfer learning wins")
print("=" * 55)

print(f"""
  FROM SCRATCH:
    - Need millions of images
    - Train for hours/days on GPU
    - Learn edges, shapes, objects from zero
    - Risk: not enough data -> overfitting

  TRANSFER LEARNING:
    - Need only hundreds/thousands of images
    - Train for minutes (only last layer)
    - Reuse edges, shapes, objects already learned
    - Works: pretrained features are universal

  In practice, almost ALL modern image classification
  uses transfer learning. Nobody trains from scratch.
""")


# ============================================================
# SUMMARY
# ============================================================
print(f"{'='*55}")
print("SUMMARY - What you learned in Lab 09:")
print(f"{'='*55}")

print(f"""
  1. TRANSFER LEARNING = reuse a pretrained network
     Load ResNet18 (trained on 1.2M images),
     freeze layers, replace last layer for your task.

  2. DATA AUGMENTATION = make training data varied
     RandomHorizontalFlip, Resize, Normalize.
     Helps the model generalize better.

  3. Only train the LAST LAYER
     {trainable} trainable params out of {total_params:,} total.
     Fast training, great results!

  4. OxfordIIITPet: real pet photos, auto-download.
     Simplified to binary: cat vs dog.

  Next: Saving and loading models - don't lose
  your trained network!
""")
