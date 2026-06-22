"""
LAB 13: GENERATIVE AI - Text Generation with GPT-2
====================================================
Lab 11: we built a tiny LSTM that classifies sentiment.
Lab 12: we learned about attention and Transformers.
Lab 13: let's USE a real Transformer to GENERATE text!

We'll load GPT-2 (124 million parameters) from Hugging Face.
It was trained on 40GB of internet text by OpenAI (2019).
Small by today's standards, but perfect to see GenAI in action.

HOW IT WORKS:
  GPT-2 does ONE thing: predict the NEXT word.
  Give it "The cat sat on the" -> it predicts "mat".
  Then feed "The cat sat on the mat" -> it predicts "and".
  Repeat -> you get a whole paragraph. That's text generation!

REQUIREMENTS:
  pip install transformers
  (First run downloads ~500MB model files)
"""

import torch

# ============================================================
# STEP 1: LOAD GPT-2
# ============================================================
print("=" * 55)
print("STEP 1: Loading GPT-2 from Hugging Face")
print("=" * 55)

print("""
  Hugging Face = the "GitHub of AI models."
  Thousands of pretrained models, free to download.

  GPT-2 Small:
    - 124 million parameters
    - 12 attention layers
    - Trained on 40GB of text (books, Wikipedia, web)
    - Released by OpenAI in 2019

  Loading (downloads ~500MB on first run)...
""")

from transformers import GPT2LMHeadModel, GPT2Tokenizer

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2').to(device)
model.eval()

total_params = sum(p.numel() for p in model.parameters())
print(f"  Model loaded!")
print(f"  Parameters: {total_params:,} ({total_params/1e6:.0f}M)")
print(f"  Vocabulary: {tokenizer.vocab_size:,} tokens")
print(f"  Device: {device}")

input("\n  Press Enter to see how tokenization works...")


# ============================================================
# STEP 2: TOKENIZATION (text -> numbers for the model)
# ============================================================
print("\n" + "=" * 55)
print("STEP 2: Tokenization")
print("=" * 55)

print("""
  In Lab 11, we split text into words: "I love this" -> ["I", "love", "this"]
  GPT-2 uses SUBWORD tokens (called BPE - Byte Pair Encoding).

  Why? It handles ANY word, even ones it never saw:
    "unhappiness" -> ["un", "happiness"]
    "ChatGPT"     -> ["Chat", "GPT"]

  Let's see:
""")

examples = [
    "Hello world",
    "Artificial intelligence is amazing",
    "The quick brown fox jumps over the lazy dog",
    "Neural networks learn from data",
]

for text in examples:
    tokens = tokenizer.encode(text)
    decoded = [tokenizer.decode([t]) for t in tokens]
    print(f"  '{text}'")
    print(f"    Token IDs: {tokens}")
    print(f"    Tokens:    {decoded}")
    print()

input("  Press Enter to see next-token prediction...")


# ============================================================
# STEP 3: NEXT TOKEN PREDICTION (the core of GPT)
# ============================================================
print("\n" + "=" * 55)
print("STEP 3: Next-token prediction")
print("=" * 55)

print("""
  GPT-2's ONLY job: given some words, predict the NEXT one.

  "The cat sat on the" -> ???

  It outputs a probability for EVERY token in its vocabulary
  (50,257 tokens!). The highest probability = best guess.
""")

prompt = "The cat sat on the"
input_ids = tokenizer.encode(prompt, return_tensors='pt').to(device)

with torch.no_grad():
    outputs = model(input_ids)
    next_token_logits = outputs.logits[0, -1, :]  # last position
    probs = torch.softmax(next_token_logits, dim=0)

# Top 10 predictions
top_probs, top_ids = torch.topk(probs, 10)

print(f"  Prompt: '{prompt}'\n")
print(f"  Top 10 predictions for the next token:\n")
print(f"  {'Rank':>5} | {'Token':>12} | {'Probability':>12}")
print(f"  {'-'*38}")
for rank, (prob, token_id) in enumerate(zip(top_probs, top_ids)):
    token_text = tokenizer.decode([token_id.item()])
    bar = "#" * int(prob.item() * 80)
    print(f"  {rank+1:>5} | {repr(token_text):>12} | {prob.item():>11.1%}  {bar}")

print(f"""
  The model thinks '{tokenizer.decode([top_ids[0].item()])}' is most likely!
  It learned this from reading billions of sentences.
""")

input("  Press Enter to generate text...")


# ============================================================
# STEP 4: TEXT GENERATION
# ============================================================
print("\n" + "=" * 55)
print("STEP 4: Generate text (autoregressive decoding)")
print("=" * 55)

print("""
  Generation = repeat next-token prediction in a loop:

    1. "The cat"           -> predict "sat"
    2. "The cat sat"       -> predict "on"
    3. "The cat sat on"    -> predict "the"
    4. "The cat sat on the" -> predict "mat"
    ...keep going!

  This is called AUTOREGRESSIVE generation.
  Let's try several prompts:
""")

prompts = [
    "Once upon a time",
    "The future of artificial intelligence",
    "In a galaxy far far away",
    "The best way to learn programming is",
]

# Set pad token to avoid warning
tokenizer.pad_token = tokenizer.eos_token

for prompt in prompts:
    input_ids = tokenizer.encode(prompt, return_tensors='pt').to(device)
    attention_mask = torch.ones_like(input_ids)

    with torch.no_grad():
        output = model.generate(
            input_ids,
            attention_mask=attention_mask,
            max_new_tokens=40,
            do_sample=True,
            temperature=0.8,
            top_k=50,
            pad_token_id=tokenizer.eos_token_id,
        )

    generated = tokenizer.decode(output[0], skip_special_tokens=True)
    print(f"  Prompt: '{prompt}'")
    print(f"  Output: {generated}")
    print()

input("  Press Enter to explore temperature...")


# ============================================================
# STEP 5: TEMPERATURE - Creativity vs Predictability
# ============================================================
print("\n" + "=" * 55)
print("STEP 5: Temperature control")
print("=" * 55)

print("""
  TEMPERATURE controls how "creative" the model is:

    Low  (0.2): picks the most likely token -> safe, repetitive
    Mid  (0.8): balanced -> coherent but varied
    High (1.5): picks unlikely tokens too -> wild, creative

  Same prompt, different temperatures:
""")

prompt = "The secret to happiness is"
input_ids = tokenizer.encode(prompt, return_tensors='pt').to(device)
attention_mask = torch.ones_like(input_ids)

for temp in [0.2, 0.8, 1.5]:
    label = {0.2: "LOW  (safe)", 0.8: "MID  (balanced)", 1.5: "HIGH (creative)"}[temp]

    with torch.no_grad():
        output = model.generate(
            input_ids,
            attention_mask=attention_mask,
            max_new_tokens=30,
            do_sample=True,
            temperature=temp,
            top_k=50,
            pad_token_id=tokenizer.eos_token_id,
        )

    generated = tokenizer.decode(output[0], skip_special_tokens=True)
    print(f"  Temp {temp} ({label}):")
    print(f"    {generated}")
    print()

print("""
  Low temperature  -> "plays it safe", picks obvious words
  High temperature -> "takes risks", more surprising output
  This is the SAME knob you see in ChatGPT/Claude settings!
""")

input("  Press Enter to try interactive generation...")


# ============================================================
# STEP 6: INTERACTIVE GENERATION
# ============================================================
print("\n" + "=" * 55)
print("STEP 6: Your turn! (type a prompt)")
print("=" * 55)

print("""
  Type any prompt and GPT-2 will continue it.
  Type 'quit' to exit.
""")

while True:
    user_prompt = input("  Your prompt (or 'quit'): ").strip()
    if user_prompt.lower() in ('quit', 'q', 'exit', ''):
        break

    input_ids = tokenizer.encode(user_prompt, return_tensors='pt').to(device)
    attention_mask = torch.ones_like(input_ids)

    with torch.no_grad():
        output = model.generate(
            input_ids,
            attention_mask=attention_mask,
            max_new_tokens=50,
            do_sample=True,
            temperature=0.8,
            top_k=50,
            pad_token_id=tokenizer.eos_token_id,
        )

    generated = tokenizer.decode(output[0], skip_special_tokens=True)
    print(f"\n  GPT-2: {generated}\n")

print()


# ============================================================
# STEP 7: HOW DOES GPT-2 RELATE TO ChatGPT/Claude?
# ============================================================
print("=" * 55)
print("STEP 7: From GPT-2 to ChatGPT and Claude")
print("=" * 55)

print("""
  GPT-2 (what we just used):
    - 124M parameters
    - Trained on 40GB of text
    - Just predicts next token (no chat ability)
    - Released 2019

  GPT-4 / Claude:
    - Hundreds of BILLIONS of parameters
    - Trained on TRILLIONS of tokens
    - Fine-tuned with human feedback (RLHF)
    - Can follow instructions, chat, reason

  The CORE is the same: predict the next token.
  The difference:
    1. SCALE: 1000x more parameters + data
    2. RLHF: humans rated outputs -> model learned
       what's helpful, honest, and harmless
    3. INSTRUCTION TUNING: trained on conversations,
       not just raw text

  GPT-2 generates plausible text.
  ChatGPT/Claude generate USEFUL, ALIGNED text.
""")


# ============================================================
# SUMMARY
# ============================================================
print(f"{'='*55}")
print("SUMMARY - What you learned in Lab 13:")
print(f"{'='*55}")

print(f"""
  1. HUGGING FACE = model hub with thousands of pretrained models
     Two lines to load: Tokenizer + Model. That's it.

  2. TOKENIZATION = text -> subword token IDs
     BPE handles any word, even invented ones.

  3. NEXT-TOKEN PREDICTION = the core of all GPT models
     Output probabilities for 50,257 tokens, pick one, repeat.

  4. AUTOREGRESSIVE GENERATION = predict one token at a time
     Feed output back as input. Loop until done.

  5. TEMPERATURE = creativity dial
     Low (0.2) = safe/repetitive. High (1.5) = wild/creative.

  6. GPT-2 -> ChatGPT/Claude = same idea, massive scale + RLHF

  THE COMPLETE JOURNEY (13 labs):
    01-03: Neurons and layers          (foundations)
    04-05: NumPy and PyTorch           (tools)
    06-08: MNIST, overfitting, CNN     (images)
    09-10: Transfer learning, saving   (practical skills)
    11:    RNN/LSTM                    (text)
    12:    Attention + Transformers    (theory)
    13:    GPT-2 text generation       (GenAI in action!)

  You've gone from a single neuron to generating text
  with a 124-million-parameter Transformer. Well done!
""")
