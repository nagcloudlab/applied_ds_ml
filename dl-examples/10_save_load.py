"""
LAB 10: SAVE AND LOAD MODELS
==============================
You trained 3 hours. Save your brain so you don't re-study.

In real projects, you:
  1. Train a model (minutes to days)
  2. SAVE it to a file
  3. Load it later for predictions (no retraining!)
  4. Save CHECKPOINTS during training (resume if interrupted)

This lab teaches the essential skill of model persistence.
"""

import torch
import torch.nn as nn
from torchvision import datasets, transforms
import os

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# ============================================================
# STEP 1: TRAIN A MODEL (quick MNIST)
# ============================================================
print("=" * 55)
print("STEP 1: Train a model to save")
print("=" * 55)

print("""
  First, let's train a small MNIST model for 2 epochs.
  Then we'll save it, delete it, and bring it back!
""")

transform = transforms.ToTensor()
train_data = datasets.MNIST('data', train=True, download=True, transform=transform)
test_data = datasets.MNIST('data', train=False, download=True, transform=transform)

train_loader = torch.utils.data.DataLoader(train_data, batch_size=64, shuffle=True)
test_loader = torch.utils.data.DataLoader(test_data, batch_size=1000)

model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(784, 128),
    nn.ReLU(),
    nn.Linear(128, 10),
).to(device)

loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

print(f"  Training for 2 epochs...\n")

for epoch in range(2):
    model.train()
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        loss = loss_fn(model(images), labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    model.eval()
    correct = total = 0
    with torch.no_grad():
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            correct += (model(images).argmax(1) == labels).sum().item()
            total += labels.size(0)
    acc = correct / total * 100
    print(f"  Epoch {epoch+1}/2 | Test accuracy: {acc:.1f}%")

trained_acc = acc
print(f"\n  Model trained! Test accuracy: {trained_acc:.1f}%")

input("\n  Press Enter to save the model...")


# ============================================================
# STEP 2: SAVE THE MODEL
# ============================================================
print("\n" + "=" * 55)
print("STEP 2: Save the model")
print("=" * 55)

print("""
  Two ways to save:

  1. Save WEIGHTS ONLY (recommended):
     torch.save(model.state_dict(), 'model.pth')
     - Smaller file, more flexible
     - Need to recreate the model architecture to load

  2. Save ENTIRE model (architecture + weights):
     torch.save(model, 'model_full.pth')
     - Bigger file, less portable
     - Can load without knowing the architecture
""")

save_dir = os.path.join(os.path.dirname(__file__), 'saved_models')
os.makedirs(save_dir, exist_ok=True)

save_path = os.path.join(save_dir, 'mnist_model.pth')
torch.save(model.state_dict(), save_path)

file_size = os.path.getsize(save_path) / 1024
print(f"  Saved to: {save_path}")
print(f"  File size: {file_size:.1f} KB")

# Show what's inside
state = model.state_dict()
print(f"\n  What's in state_dict():")
for name, tensor in state.items():
    print(f"    {name:>10}: shape {list(tensor.shape)}")

input("\n  Press Enter to delete and reload...")


# ============================================================
# STEP 3: LOAD THE MODEL
# ============================================================
print("\n" + "=" * 55)
print("STEP 3: Delete and reload the model")
print("=" * 55)

print("""
  Let's prove the save worked:
    1. Delete the model from memory
    2. Create a FRESH model (random weights)
    3. Load the saved weights
    4. Check accuracy matches!
""")

# Delete the trained model
del model
print(f"  Model deleted from memory!")

# Create fresh model (random weights)
fresh_model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(784, 128),
    nn.ReLU(),
    nn.Linear(128, 10),
).to(device)

# Check accuracy BEFORE loading (should be ~10%, random)
fresh_model.eval()
correct = total = 0
with torch.no_grad():
    for images, labels in test_loader:
        images, labels = images.to(device), labels.to(device)
        correct += (fresh_model(images).argmax(1) == labels).sum().item()
        total += labels.size(0)
random_acc = correct / total * 100
print(f"  Fresh model accuracy (random weights): {random_acc:.1f}%")

# Load saved weights
fresh_model.load_state_dict(torch.load(save_path, weights_only=True))
print(f"  Loaded weights from: {save_path}")

# Check accuracy AFTER loading
fresh_model.eval()
correct = total = 0
with torch.no_grad():
    for images, labels in test_loader:
        images, labels = images.to(device), labels.to(device)
        correct += (fresh_model(images).argmax(1) == labels).sum().item()
        total += labels.size(0)
loaded_acc = correct / total * 100
print(f"  Loaded model accuracy: {loaded_acc:.1f}%")

print(f"\n  Before save: {trained_acc:.1f}% | After load: {loaded_acc:.1f}% | Match!")

input("\n  Press Enter to learn about checkpoints...")


# ============================================================
# STEP 4: CHECKPOINTS (save during training)
# ============================================================
print("\n" + "=" * 55)
print("STEP 4: Checkpoints (save training progress)")
print("=" * 55)

print("""
  What if training takes 10 hours and crashes at hour 8?
  CHECKPOINTS save everything needed to RESUME training:
    - Model weights
    - Optimizer state (learning rate momentum, etc.)
    - Current epoch
    - Current loss

  Save a checkpoint every N epochs. If it crashes,
  load the last checkpoint and continue!
""")

# Demo: save a checkpoint
model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(784, 128),
    nn.ReLU(),
    nn.Linear(128, 10),
).to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

checkpoint_path = os.path.join(save_dir, 'checkpoint.pth')

checkpoint = {
    'epoch': 5,
    'model_state_dict': model.state_dict(),
    'optimizer_state_dict': optimizer.state_dict(),
    'loss': 0.234,
}
torch.save(checkpoint, checkpoint_path)

print(f"  Saved checkpoint with:")
for key in checkpoint:
    if key.endswith('_dict'):
        print(f"    {key}: ({len(checkpoint[key])} entries)")
    else:
        print(f"    {key}: {checkpoint[key]}")

# Demo: load checkpoint
print(f"\n  Loading checkpoint to resume training:")
loaded_ckpt = torch.load(checkpoint_path, weights_only=False)
model.load_state_dict(loaded_ckpt['model_state_dict'])
optimizer.load_state_dict(loaded_ckpt['optimizer_state_dict'])
resume_epoch = loaded_ckpt['epoch']
print(f"    Resume from epoch {resume_epoch}, loss was {loaded_ckpt['loss']}")

input("\n  Press Enter to predict with saved model...")


# ============================================================
# STEP 5: PREDICT WITH LOADED MODEL
# ============================================================
print(f"\n{'='*55}")
print("STEP 5: Use the loaded model for predictions")
print("=" * 55)

# Load the good model
model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(784, 128),
    nn.ReLU(),
    nn.Linear(128, 10),
).to(device)
model.load_state_dict(torch.load(save_path, weights_only=True))
model.eval()

test_images, test_labels = next(iter(test_loader))
test_images, test_labels = test_images.to(device), test_labels.to(device)

with torch.no_grad():
    outputs = model(test_images[:5])
    preds = outputs.argmax(1)
    probs = torch.softmax(outputs, dim=1)

print(f"\n  5 predictions from the LOADED model:\n")
for i in range(5):
    actual = test_labels[i].item()
    pred = preds[i].item()
    conf = probs[i][pred].item()
    status = "OK" if pred == actual else "WRONG"
    print(f"    Image {i+1}: actual={actual}, predicted={pred} ({conf:.0%}) {status}")

# Clean up saved files
print(f"\n  (Saved model files are in: {save_dir})")


# ============================================================
# SUMMARY
# ============================================================
print(f"\n{'='*55}")
print("SUMMARY - What you learned in Lab 10:")
print(f"{'='*55}")

print("""
  1. SAVE weights:  torch.save(model.state_dict(), 'model.pth')
     Load weights:  model.load_state_dict(torch.load('model.pth'))

  2. CHECKPOINT = save model + optimizer + epoch + loss
     Lets you resume training after crashes.

  3. state_dict() = dictionary of all learned weights
     Smaller, more portable than saving the whole model.

  4. Always call model.eval() before predictions!
     Disables dropout and batch normalization training behavior.

  Next: Text and RNNs - teaching a network to READ.
  Sequential data, word embeddings, and LSTM memory.
""")
