"""
LAB 11: TEACH A NETWORK TO READ (Text Classification with RNN)
================================================================
Lab 06-08: images (pixels)  -> CNN  -> "what digit/animal is this?"
Lab 11:    text   (words)   -> RNN  -> "is this positive or negative?"

THE BIG SHIFT:
  Images: all pixels exist AT ONCE (2D grid)
  Text:   words come in SEQUENCE (one after another)

  "I love this movie" -> positive
  "I hate this movie" -> negative
  The ORDER of words matters!

WHAT'S NEW:
  1. Tokenization (text -> word IDs)
  2. Word Embeddings (each word becomes a vector)
  3. LSTM (reads sequences with memory)
"""

import torch
import torch.nn as nn
import random

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# ============================================================
# STEP 1: TEXT IS NOT NUMBERS + TRAINING DATA
# ============================================================
print("=" * 55)
print("STEP 1: Text to numbers")
print("=" * 55)

print("""
  Neural networks only understand NUMBERS.
  How to convert "I love this movie" to numbers?

    1. TOKENIZE:  "I love this movie" -> ["I", "love", "this", "movie"]
    2. VOCABULARY: give each word an ID  {"I": 2, "love": 3, ...}
    3. CONVERT:   ["I", "love", "this", "movie"] -> [2, 3, 4, 5]
""")

train_texts = [
    ("this movie is great", 1), ("i love this film", 1),
    ("amazing story and acting", 1), ("really good movie", 1),
    ("wonderful film loved it", 1), ("best movie ever made", 1),
    ("great acting great story", 1), ("this film is amazing", 1),
    ("loved every moment", 1), ("excellent movie must watch", 1),
    ("brilliant performance by actors", 1), ("fantastic story telling", 1),
    ("highly recommend this film", 1), ("so good and fun", 1),
    ("beautiful movie enjoyed it", 1),
    ("this movie is terrible", 0), ("i hate this film", 0),
    ("boring story bad acting", 0), ("really bad movie", 0),
    ("awful film hated it", 0), ("worst movie ever made", 0),
    ("bad acting bad story", 0), ("this film is boring", 0),
    ("hated every moment", 0), ("terrible movie avoid it", 0),
    ("poor performance by actors", 0), ("waste of time watching", 0),
    ("do not watch this film", 0), ("so bad and boring", 0),
    ("horrible movie regret watching", 0),
]

random.seed(42)
random.shuffle(train_texts)

print(f"  {len(train_texts)} movie reviews (15 positive, 15 negative)\n")
for text, label in train_texts[:6]:
    print(f"    {'POS' if label else 'NEG'}: {text}")
print(f"    ... and {len(train_texts)-6} more")

input("\n  Press Enter to build vocabulary...")


# ============================================================
# STEP 2: BUILD VOCABULARY
# ============================================================
print("\n" + "=" * 55)
print("STEP 2: Building the vocabulary")
print("=" * 55)

word_to_id = {"<PAD>": 0, "<UNK>": 1}

for text, _ in train_texts:
    for word in text.lower().split():
        if word not in word_to_id:
            word_to_id[word] = len(word_to_id)

vocab_size = len(word_to_id)

print(f"\n  Vocabulary size: {vocab_size} words")
print(f"  Sample: ", end="")
shown = list(word_to_id.items())[:8]
print(", ".join(f"'{w}'={i}" for w, i in shown))


def text_to_ids(text, max_len=8):
    words = text.lower().split()
    ids = [word_to_id.get(w, 1) for w in words]
    if len(ids) < max_len:
        ids = ids + [0] * (max_len - len(ids))
    else:
        ids = ids[:max_len]
    return ids


example = "i love this movie"
ids = text_to_ids(example)
print(f"\n  '{example}' -> {ids}")
print(f"  (zeros = padding to make all sentences same length)")

input("\n  Press Enter to learn about embeddings...")


# ============================================================
# STEP 3: WORD EMBEDDINGS
# ============================================================
print("\n" + "=" * 55)
print("STEP 3: Word embeddings")
print("=" * 55)

print("""
  Word ID "3" and ID "4" are just numbers.
  The network doesn't know they're related!

  EMBEDDINGS: each word gets a VECTOR that captures meaning.
  Similar words -> similar vectors (learned during training).

    "movie" -> [0.2, 0.8, 0.1, 0.5]
    "film"  -> [0.3, 0.7, 0.2, 0.4]   (similar!)
    "hate"  -> [0.9, 0.1, 0.8, 0.2]   (different!)
""")

embedding_dim = 16
embedding = nn.Embedding(vocab_size, embedding_dim, padding_idx=0)

sample_ids = torch.tensor([text_to_ids("i love this movie")])
embedded = embedding(sample_ids)

print(f"  nn.Embedding({vocab_size}, {embedding_dim})")
print(f"  Each word becomes a vector of {embedding_dim} numbers.")
print(f"  Input shape:  {list(sample_ids.shape)} (1 sentence, 8 words)")
print(f"  Output shape: {list(embedded.shape)} (+ {embedding_dim} numbers per word)")

input("\n  Press Enter to learn about LSTM...")


# ============================================================
# STEP 4: LSTM - READING WITH MEMORY
# ============================================================
print("\n" + "=" * 55)
print("STEP 4: LSTM - reading word by word with memory")
print("=" * 55)

print("""
  CNN scans IMAGES with filters.
  LSTM reads TEXT word by word, keeping a "memory":

    Step 1: read "I"     -> memory: "someone speaking"
    Step 2: read "love"  -> memory: "someone loves something"
    Step 3: read "this"  -> memory: "someone loves this thing"
    Step 4: read "movie" -> memory: "someone loves this movie" = POSITIVE!

  The FINAL memory captures the sentence meaning.

  Why LSTM, not plain RNN?
    RNN forgets early words in long sentences.
    LSTM has a "cell state" - a highway for information.
    It CHOOSES what to remember and what to forget.
""")

input("  Press Enter to build the full model...")


# ============================================================
# STEP 5: BUILD THE MODEL
# ============================================================
print("\n" + "=" * 55)
print("STEP 5: Build the LSTM model")
print("=" * 55)

class SentimentRNN(nn.Module):
    def __init__(self, vocab_size, embed_dim, hidden_dim):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=0)
        self.lstm = nn.LSTM(embed_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        embedded = self.embedding(x)
        output, (hidden, cell) = self.lstm(embedded)
        hidden = hidden.squeeze(0)
        return self.sigmoid(self.fc(hidden))

model = SentimentRNN(vocab_size, embed_dim=16, hidden_dim=32).to(device)
total_params = sum(p.numel() for p in model.parameters())

print(f"""
  Pipeline:
    "i love this movie"
      -> word IDs       [2, 3, 4, 5, 0, 0, 0, 0]
      -> embeddings     each ID becomes 16 numbers
      -> LSTM           reads word by word, builds memory
      -> final memory   captures sentence meaning
      -> Linear+Sigmoid positive (>0.5) or negative (<0.5)?

  Total parameters: {total_params:,}
""")

input("  Press Enter to train...")


# ============================================================
# STEP 6: TRAIN
# ============================================================
print("\n" + "=" * 55)
print("STEP 6: Training")
print("=" * 55)

X_train = torch.tensor([text_to_ids(t) for t, _ in train_texts]).to(device)
y_train = torch.tensor([[l] for _, l in train_texts], dtype=torch.float32).to(device)

model = SentimentRNN(vocab_size, embed_dim=16, hidden_dim=32).to(device)
loss_fn = nn.BCELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

print(f"\n  {'Epoch':>6} | {'Loss':>8} | {'Accuracy':>9}")
print(f"  {'-'*35}")

for epoch in range(201):
    model.train()
    pred = model(X_train)
    loss = loss_fn(pred, y_train)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    with torch.no_grad():
        accuracy = ((pred >= 0.5).float() == y_train).sum().item() / len(y_train) * 100

    if epoch % 25 == 0 or epoch == 200:
        print(f"  {epoch:>6} | {loss.item():>8.4f} | {accuracy:>8.1f}%")

input("\n  Press Enter to test...")


# ============================================================
# STEP 7: TEST ON NEW REVIEWS
# ============================================================
print(f"\n{'='*55}")
print("STEP 7: Test on new reviews")
print("=" * 55)

test_reviews = [
    "i love this movie", "this film is terrible",
    "great movie loved it", "bad acting boring story",
    "really amazing film", "worst movie ever",
    "fantastic must watch", "awful waste of time",
    "good story great acting", "horrible film hated it",
]

model.eval()
print(f"\n  {'Review':<30} {'Prob':>6} {'Prediction':>12}")
print(f"  {'-'*52}")

with torch.no_grad():
    for review in test_reviews:
        ids = text_to_ids(review)
        input_t = torch.tensor([ids]).to(device)
        prob = model(input_t).item()
        pred = "POSITIVE" if prob >= 0.5 else "NEGATIVE"
        bar = "#" * int(prob * 20)
        print(f"  {review:<30} {prob:>5.0%} {pred:>12}  {bar}")

input("\n  Press Enter to check embeddings...")


# ============================================================
# STEP 8: DID EMBEDDINGS LEARN MEANING?
# ============================================================
print(f"\n{'='*55}")
print("STEP 8: Did embeddings learn word meaning?")
print("=" * 55)

def word_distance(w1, w2):
    id1 = word_to_id.get(w1, 1)
    id2 = word_to_id.get(w2, 1)
    v1 = model.embedding.weight[id1].detach()
    v2 = model.embedding.weight[id2].detach()
    return torch.dist(v1, v2).item()

pairs = [
    ("love", "great", "both positive"),
    ("hate", "terrible", "both negative"),
    ("love", "hate", "opposites"),
    ("movie", "film", "synonyms"),
    ("good", "bad", "opposites"),
]

print(f"\n  {'Word 1':<10} {'Word 2':<10} {'Distance':>10}  Note")
print(f"  {'-'*48}")
for w1, w2, note in pairs:
    dist = word_distance(w1, w2)
    bar = "#" * int(dist * 3)
    print(f"  {w1:<10} {w2:<10} {dist:>10.2f}  {bar} {note}")

print("""
  Similar words (love/great) should have small distance.
  Opposite words (love/hate) should have large distance.
  The network learned this from just 30 reviews!
""")


# ============================================================
# SUMMARY
# ============================================================
print(f"{'='*55}")
print("SUMMARY - What you learned in Lab 11:")
print(f"{'='*55}")

print("""
  1. TEXT -> NUMBERS: Tokenize -> Vocabulary -> Word IDs

  2. EMBEDDINGS = words as vectors
     Similar words get similar vectors (learned automatically).

  3. LSTM = reads sequences with memory
     Processes one word at a time, final memory = sentence meaning.

  4. Different data, different architecture:
     Images -> CNN (spatial patterns)
     Text   -> LSTM (sequential patterns)

  LIMITATIONS of our tiny model:
    - Struggles with negation ("not good")
    - Can't handle sarcasm or complex context
    - Real models (BERT, GPT) train on billions of words

  Next: Attention, Transformers, and the GenAI revolution.
  The architecture behind ChatGPT and modern AI.
""")
