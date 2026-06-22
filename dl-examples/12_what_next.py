"""
LAB 12: WHAT'S NEXT - Attention, Transformers, and GenAI
=========================================================
You've come an incredible distance in 11 labs.
Let's look at what comes AFTER everything you've learned,
and the technologies powering today's AI revolution.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F

# ============================================================
# STEP 1: THE JOURNEY SO FAR
# ============================================================
print("=" * 55)
print("STEP 1: Your deep learning journey (11 labs!)")
print("=" * 55)

print("""
  +-----+---------------------------+---------------------------+
  | Lab | Topic                     | Key Concept               |
  +-----+---------------------------+---------------------------+
  |  01 | Single Neuron             | multiply + add + sigmoid  |
  |  02 | Activation Functions      | ReLU, Sigmoid, Tanh       |
  |  03 | Hidden Layer              | layers solve harder tasks  |
  |  04 | NumPy Network             | X @ W + b (matrix math)   |
  |  05 | PyTorch Intro             | autograd, nn.Sequential   |
  |  06 | MNIST Digits              | DataLoader, multi-class   |
  |  07 | Overfitting               | Dropout, Early Stopping   |
  |  08 | CNN                       | conv filters, pooling     |
  |  09 | Cat vs Dog                | transfer learning         |
  |  10 | Save/Load Models          | checkpoints, state_dict   |
  |  11 | Text RNN/LSTM             | embeddings, sequences     |
  |  12 | This lab!                 | attention, Transformers   |
  |  13 | GenAI Text Generation     | GPT-2, Hugging Face       |
  +-----+---------------------------+---------------------------+

  You understand: neurons, layers, backpropagation,
  CNNs for images, RNNs for text, and practical skills
  like saving models and preventing overfitting.
""")

input("  Press Enter to see what's next...")


# ============================================================
# STEP 2: THE PROBLEM WITH RNNs
# ============================================================
print("\n" + "=" * 55)
print("STEP 2: Why we moved beyond RNNs")
print("=" * 55)

print("""
  RNNs read word by word. Two big problems:

  1. SLOW: must process word 5 AFTER words 1-4 (sequential)
     Can't use GPU parallelism efficiently.

  2. FORGETFUL: by word 50, the memory of word 1 is faint.
     "The cat, which was sitting on the mat that my grandmother
      bought from the store near the park, was ___."
     -> By the time we reach "was", we forgot "cat"!

  ATTENTION solves both problems:
    "Don't read word by word. Look at ALL words at once,
     and learn which ones to PAY ATTENTION to."
""")

input("  Press Enter to see attention in action...")


# ============================================================
# STEP 3: SELF-ATTENTION (with real numbers!)
# ============================================================
print("\n" + "=" * 55)
print("STEP 3: Self-attention demo")
print("=" * 55)

print("""
  Sentence: "The cat sat down"

  For each word, attention asks:
  "Which OTHER words should I pay attention to?"

  Let's compute it with real numbers!
""")

# Simple 4-word example with small embedding dim
words = ["The", "cat", "sat", "down"]
# Pretend embeddings (4 words, 4-dim vectors)
torch.manual_seed(42)
embeddings = torch.randn(4, 4)

print(f"  Word embeddings (4 words, 4 dimensions):")
for i, w in enumerate(words):
    vals = [f"{v:.2f}" for v in embeddings[i].tolist()]
    print(f"    '{w:>4}': [{', '.join(vals)}]")

# Compute attention scores: how much does each word attend to each other?
# Simple dot-product attention: score = q . k / sqrt(d)
d_k = embeddings.shape[1]
scores = embeddings @ embeddings.T / (d_k ** 0.5)

print(f"\n  Attention scores (dot product / sqrt({d_k})):")
print(f"         {'    '.join(f'{w:>4}' for w in words)}")
for i, w in enumerate(words):
    row = [f"{scores[i][j]:>6.2f}" for j in range(4)]
    print(f"  {w:>4}:  {'  '.join(row)}")

# Softmax to get attention weights
weights = F.softmax(scores, dim=1)

print(f"\n  After softmax (attention weights - rows sum to 1.0):")
print(f"         {'    '.join(f'{w:>4}' for w in words)}")
for i, w in enumerate(words):
    row = [f"{weights[i][j]:>6.0%}" for j in range(4)]
    print(f"  {w:>4}:  {'  '.join(row)}")

print("""
  Each row shows: "how much attention does this word pay to others?"
  High weight = "this word is important for understanding me."

  This is the CORE of Transformers!
""")

input("  Press Enter to see the Transformer architecture...")


# ============================================================
# STEP 4: TRANSFORMERS
# ============================================================
print("\n" + "=" * 55)
print("STEP 4: Transformers")
print("=" * 55)

print("""
  A Transformer = self-attention stacked many times.

  Architecture (simplified):

    Input text
      |
      v
    [Embedding]           word -> vector
      |
      v
    [Self-Attention] x N  "which words matter for each word?"
      |
      v
    [Feed-Forward] x N    process each position
      |
      v
    [Output]              prediction

  Key innovations:
    1. ATTENTION: look at all words simultaneously
    2. PARALLEL: process all positions at once (fast on GPU!)
    3. SCALABLE: just add more layers + more data = better

  This is what powers:
    - GPT-4, Claude    (text generation)
    - BERT             (text understanding)
    - Vision Transformer (images, replacing CNN!)
    - Whisper           (speech recognition)
""")

input("  Press Enter to see the GenAI landscape...")


# ============================================================
# STEP 5: GENERATIVE AI LANDSCAPE
# ============================================================
print("\n" + "=" * 55)
print("STEP 5: The Generative AI landscape (2024-2025)")
print("=" * 55)

print("""
  GenAI = AI that CREATES new content.

  TEXT GENERATION:
    GPT-4, Claude, Gemini, Llama
    - Trained on trillions of words
    - Predict the next token, over and over
    - "Given 'The cat sat on the', what comes next?"
    - Scale: billions of parameters, months of training

  IMAGE GENERATION:
    DALL-E, Midjourney, Stable Diffusion
    - Diffusion models: start with noise, gradually denoise
    - Text prompt -> image
    - Not Transformers (mostly), but attention is key

  CODE GENERATION:
    GitHub Copilot, Claude Code, Cursor
    - Trained on billions of lines of code
    - Understand intent -> write code
    - You're using one right now!

  MULTIMODAL:
    GPT-4o, Gemini, Claude
    - Understand text + images + audio together
    - "Describe this image" / "What's in this chart?"

  KEY INSIGHT:
    All of these build on the foundations you learned:
    neurons, layers, backpropagation, embeddings, attention.
    The difference is SCALE: more data, more parameters,
    more compute. The core ideas are the same.
""")

input("  Press Enter for resources and next steps...")


# ============================================================
# STEP 6: NEXT STEPS + RESOURCES
# ============================================================
print("\n" + "=" * 55)
print("STEP 6: Where to go from here")
print("=" * 55)

print("""
  BEGINNER (you are here!):
    - Kaggle competitions (Titanic, House Prices)
    - Fast.ai course (free, practical)
    - PyTorch tutorials (pytorch.org)

  INTERMEDIATE:
    - Hugging Face Transformers library
    - Fine-tune a pretrained language model
    - Build a simple chatbot with an API

  ADVANCED:
    - Read "Attention Is All You Need" paper (2017)
    - Train your own small language model
    - Explore reinforcement learning (RLHF)

  PRACTICAL SKILLS:
    - Use AI APIs (Claude, GPT) in your projects
    - Prompt engineering
    - RAG (Retrieval-Augmented Generation)
    - MLOps: deploy models to production
""")


# ============================================================
# SUMMARY
# ============================================================
print(f"{'='*55}")
print("FINAL SUMMARY - Your Deep Learning Journey")
print(f"{'='*55}")

print("""
  You started with a SINGLE NEURON (multiply + add + sigmoid).
  You built up to REAL image classifiers and text analyzers.

  The path you walked:
    Neuron -> Layer -> Network -> PyTorch -> CNN -> RNN -> ...

  What comes next:
    ... -> Attention -> Transformers -> GPT/Claude -> ???

  The field moves fast, but the FOUNDATIONS don't change:
    - Forward pass: compute predictions
    - Loss: measure how wrong
    - Backward pass: compute gradients
    - Update: improve weights
    - Repeat.

  Every AI system, from a single neuron to GPT-4,
  follows this same loop. You understand it now.

  Next: Lab 13 - generate text with a REAL Transformer (GPT-2)!
""")
