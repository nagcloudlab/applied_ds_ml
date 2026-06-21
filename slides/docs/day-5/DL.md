# From Machine Learning to Deep Learning

## Why Neural Networks Became Important

---

## Slide 1: Title

# From Machine Learning to Deep Learning

### Why Neural Networks Became Important

---

## Slide 2: Learning Goals

By the end, students should understand:

* Advantages of classical ML models
* Limitations of classical ML
* Why Deep Learning is needed
* What a neural network is
* How neural networks learn
* Types of neural networks
* When to use ML vs DL

---

## Slide 3: Big Picture

# ML to DL Journey

Classical ML:

Structured data → Manual features → Model → Prediction

Deep Learning:

Raw data → Neural network learns features → Prediction

---

## Slide 4: Where We Are

Already covered:

| ML Area        | Examples                           |
| -------------- | ---------------------------------- |
| Regression     | Linear, Multiple Linear Regression |
| Classification | Logistic Regression, Trees, SVM    |
| Clustering     | K-Means                            |

Now:

Deep Learning and Neural Networks

---

## Slide 5: Section Divider

# Part 1

## Classical Machine Learning Recap

---

## Slide 6: Classical ML Meaning

Classical ML models learn patterns from structured data.

Example:

| Study Hours | Attendance | Previous Score | Result |
| ----------: | ---------: | -------------: | ------ |
|           5 |         80 |             60 | Pass   |

The features are already prepared.

---

## Slide 7: Classical ML Flow

Feature Engineering → Model Training → Prediction

Example:

Study Hours + Attendance + Previous Score → Pass / Fail

Human prepares useful columns.

Model learns from those columns.

---

## Slide 8: Classical ML Model Examples

| Task           | Models                                  |
| -------------- | --------------------------------------- |
| Regression     | Linear Regression, Ridge, Random Forest |
| Classification | Logistic Regression, SVM, Random Forest |
| Clustering     | K-Means                                 |

---

## Slide 9: Section Divider

# Part 2

## Advantages of Classical ML Models

---

## Slide 10: Advantage 1 — Easy to Understand

Many classical ML models are explainable.

Example:

Linear Regression:

Score = 30 + 5 × Study Hours

Meaning:

Each extra study hour adds around 5 marks.

---

## Slide 11: Advantage 2 — Works Well on Tabular Data

Classical ML is strong for structured business data.

Examples:

| Dataset         | Prediction          |
| --------------- | ------------------- |
| Student records | Pass / Fail         |
| Customer table  | Churn / Not Churn   |
| Loan data       | Approved / Rejected |
| Sales table     | Future sales        |

---

## Slide 12: Advantage 3 — Needs Less Data

Classical ML can work with small or medium datasets.

Example:

A company may have 1,000 customer records.

Logistic Regression or Random Forest may work well.

Deep Learning usually needs much more data.

---

## Slide 13: Advantage 4 — Faster to Train

Classical ML models usually train faster.

Example:

| Model               | Training Need         |
| ------------------- | --------------------- |
| Logistic Regression | Low compute           |
| Decision Tree       | Low to medium compute |
| Random Forest       | Medium compute        |
| Deep Neural Network | Higher compute        |

---

## Slide 14: Advantage 5 — Easier Debugging

Classical ML is often easier to inspect.

Examples:

| Model               | Explanation                   |
| ------------------- | ----------------------------- |
| Linear Regression   | Coefficients                  |
| Logistic Regression | Feature effect on probability |
| Decision Tree       | If-else rules                 |
| Random Forest       | Feature importance            |

---

## Slide 15: Advantage 6 — Strong Baseline

Before using complex models, start with classical ML.

Example workflow:

Baseline Model → Evaluate → Improve → Try Advanced Model

A simple model keeps us honest.

---

## Slide 16: Classical ML Strength Summary

| Advantage             | Meaning             |
| --------------------- | ------------------- |
| Explainable           | Easy to present     |
| Fast                  | Less compute        |
| Works on tabular data | Business friendly   |
| Less data required    | Practical           |
| Good baseline         | Safe starting point |

---

## Slide 17: Section Divider

# Part 3

## Limitations of Classical ML

---

## Slide 18: Limitation 1 — Manual Feature Engineering

Classical ML depends heavily on prepared features.

Example:

To predict student result, humans create:

* Study Hours
* Attendance
* Previous Score
* Practice Tests

The model learns from these columns.

---

## Slide 19: What If Data Is Raw?

Raw data examples:

| Data Type | Raw Form          |
| --------- | ----------------- |
| Image     | Pixels            |
| Text      | Words and context |
| Audio     | Waveform          |
| Video     | Frames over time  |

Classical ML struggles unless humans extract features.

---

## Slide 20: Image Example

Problem:

Classify Cat vs Dog.

Classical ML needs manually designed features:

* Ear shape
* Fur texture
* Eye position
* Color
* Edges

This is hard to design manually.

---

## Slide 21: Text Example

Problem:

Understand sentence sentiment.

Sentence:

“The movie was not bad.”

Classical ML may look at words.

But meaning depends on context.

“not bad” actually means positive.

---

## Slide 22: Audio Example

Problem:

Speech recognition.

Raw audio contains:

* Frequency
* Tone
* Speed
* Noise
* Pronunciation differences

Manual feature design becomes difficult.

---

## Slide 23: Limitation 2 — Complex Patterns

Classical ML may struggle with:

* Images
* Long text
* Speech
* Video
* Complex sensor signals
* Very high-dimensional data

---

## Slide 24: Limitation 3 — Performance Plateaus

Sometimes performance stops improving.

Even after trying:

* Better tuning
* More features
* More preprocessing
* Stronger ML models

The model may still fail on complex raw data.

---

## Slide 25: Key Transition

Classical ML is powerful when features are well prepared.

Deep Learning is powerful when the model must learn features automatically.

This is the bridge.

---

## Slide 26: Section Divider

# Part 4

## Why Deep Learning?

---

## Slide 27: Deep Learning Need

Modern AI problems often involve raw complex data.

Examples:

| Problem           | Data            |
| ----------------- | --------------- |
| Face recognition  | Images          |
| Chatbots          | Text            |
| Speech assistant  | Audio           |
| Self-driving cars | Video + sensors |
| Medical imaging   | Scans           |

---

## Slide 28: Main Difference

Classical ML:

Human designs features.

Deep Learning:

Model learns features automatically.

---

## Slide 29: Cat vs Dog Example

Classical ML:

Human extracts edges, shapes, textures.

Deep Learning:

Raw image pixels go into neural network.

Network learns:

Edges → Shapes → Parts → Object

---

## Slide 30: Feature Learning

Deep Learning learns representations layer by layer.

Example for image:

| Layer Level   | Learns       |
| ------------- | ------------ |
| Early layers  | Edges        |
| Middle layers | Shapes       |
| Later layers  | Object parts |
| Final layers  | Cat or Dog   |

---

## Slide 31: Text Understanding Example

Sentence:

“The food was amazing, but the service was slow.”

Deep Learning can learn:

* Word meaning
* Context
* Sentence structure
* Overall sentiment

---

## Slide 32: Why DL Became Popular

Deep Learning became powerful because of:

* Big data
* Better algorithms
* GPUs and TPUs
* Cloud computing
* Open-source frameworks
* Large pretrained models

---

## Slide 33: Deep Learning Strengths

| Strength                      | Meaning                      |
| ----------------------------- | ---------------------------- |
| Learns features automatically | Less manual feature design   |
| Handles raw data              | Images, text, audio          |
| Captures complex patterns     | Nonlinear relationships      |
| Scales with data              | Improves with large datasets |
| Powers GenAI                  | Text, image, code generation |

---

## Slide 34: Deep Learning Limitations

| Limitation         | Meaning                      |
| ------------------ | ---------------------------- |
| Needs more data    | Small data may not be enough |
| Needs more compute | GPU often helpful            |
| Less interpretable | Harder to explain            |
| Longer training    | More tuning required         |
| Can overfit        | Needs regularization         |

---

## Slide 35: ML vs DL Decision

Use classical ML when:

* Data is tabular
* Dataset is small or medium
* Explanation is important
* Fast training is needed

Use DL when:

* Data is image, text, audio, video
* Large data is available
* Complex patterns exist
* Feature learning is needed

---

## Slide 36: Section Divider

# Part 5

## What is a Neural Network?

---

## Slide 37: Neural Network Meaning

A neural network is a model made of connected layers.

Basic structure:

Input Layer → Hidden Layers → Output Layer

It transforms input step by step into prediction.

---

## Slide 38: Student Prediction Example

Inputs:

| Feature        |
| -------------- |
| Study Hours    |
| Attendance     |
| Previous Score |
| Practice Tests |

Output:

Pass probability

Network learns how inputs combine.

---

## Slide 39: Neural Network Structure

| Layer        | Role                     |
| ------------ | ------------------------ |
| Input Layer  | Receives features        |
| Hidden Layer | Learns internal patterns |
| Output Layer | Gives final prediction   |

---

## Slide 40: What is a Neuron?

A neuron is a small calculation unit.

It takes inputs, applies weights, adds bias, and produces output.

Formula:

z = w₁x₁ + w₂x₂ + w₃x₃ + b

Then:

output = activation(z)

---

## Slide 41: Neuron Example

Inputs:

| Feature        | Value | Weight |
| -------------- | ----: | -----: |
| Study Hours    |     6 |    0.5 |
| Attendance     |    80 |   0.03 |
| Previous Score |    60 |   0.04 |

z = 0.5(6) + 0.03(80) + 0.04(60) + b

---

## Slide 42: Weights Meaning

Weights decide feature importance.

Example:

High weight for previous score means:

Previous score strongly affects prediction.

Low weight for sleep hours means:

Sleep may have smaller effect.

---

## Slide 43: Bias Meaning

Bias is like a starting adjustment.

Formula:

z = weighted sum + bias

Bias helps the neuron shift its decision.

Similar to intercept in Linear Regression.

---

## Slide 44: Activation Function

Activation converts z into useful output.

Without activation, neural network remains mostly linear.

Activation adds nonlinearity.

This helps the network learn complex patterns.

---

## Slide 45: Common Activation Functions

| Activation | Common Use                   |
| ---------- | ---------------------------- |
| ReLU       | Hidden layers                |
| Sigmoid    | Binary classification output |
| Softmax    | Multiclass output            |
| Tanh       | Some sequence models         |

---

## Slide 46: ReLU

ReLU formula:

ReLU(x) = max(0, x)

Meaning:

If input is negative, output is 0.

If input is positive, output stays positive.

ReLU is commonly used in hidden layers.

---

## Slide 47: Sigmoid

Sigmoid converts values into probability between 0 and 1.

Used for binary classification.

Example:

Output = 0.82

Meaning:

82% probability of class 1.

---

## Slide 48: Softmax

Softmax is used for multiclass classification.

Example:

| Class | Probability |
| ----- | ----------: |
| Cat   |        0.10 |
| Dog   |        0.80 |
| Horse |        0.10 |

Prediction:

Dog

---

## Slide 49: Hidden Layers

Hidden layers learn intermediate patterns.

Example:

In image classification:

Layer 1 learns edges.

Layer 2 learns shapes.

Layer 3 learns object parts.

Final layer predicts class.

---

## Slide 50: Why “Deep”?

A neural network becomes deep when it has many hidden layers.

Shallow Network:

Input → Hidden → Output

Deep Network:

Input → Many Hidden Layers → Output

---

## Slide 51: Section Divider

# Part 6

## How Neural Networks Learn

---

## Slide 52: Training Flow

Neural network training follows:

Forward Pass → Loss Calculation → Backpropagation → Weight Update

This repeats many times.

---

## Slide 53: Forward Pass

Forward pass means:

Input moves through the network to produce prediction.

Example:

Student features → Neural network → Pass probability

---

## Slide 54: Loss Calculation

Loss measures prediction mistake.

Example:

Actual = Pass

Predicted probability = 0.40

Mistake is high.

The network needs improvement.

---

## Slide 55: Common Loss Functions

| Task                      | Loss                      |
| ------------------------- | ------------------------- |
| Regression                | MSE                       |
| Binary classification     | Binary Cross-Entropy      |
| Multiclass classification | Categorical Cross-Entropy |

---

## Slide 56: Backpropagation

Backpropagation finds how much each weight contributed to the error.

Simple meaning:

The network sends error backward and learns which weights need change.

---

## Slide 57: Optimizer

Optimizer updates weights to reduce loss.

Common optimizers:

| Optimizer        | Meaning                    |
| ---------------- | -------------------------- |
| Gradient Descent | Basic weight update        |
| SGD              | Uses mini-batches          |
| Adam             | Popular adaptive optimizer |

---

## Slide 58: Epoch

One epoch means:

The model has seen the full training dataset once.

Example:

If training runs for 20 epochs, the model goes through the dataset 20 times.

---

## Slide 59: Batch

A batch is a small group of training examples processed together.

Example:

Dataset = 10,000 records

Batch size = 32

The model updates weights after each batch.

---

## Slide 60: Learning Rate

Learning rate controls step size during weight update.

Too high:

Model may jump and fail to learn.

Too low:

Model learns very slowly.

---

## Slide 61: Training Example

Actual class:

Pass

Prediction before training:

0.40

After weight updates:

0.60

Later:

0.82

The model gradually improves.

---

## Slide 62: Overfitting in Neural Networks

Neural networks can memorize training data.

Signs:

Training accuracy high.

Validation accuracy low.

Fixes:

* More data
* Dropout
* Regularization
* Early stopping
* Data augmentation

---

## Slide 63: Section Divider

# Part 7

## Types of Neural Networks

---

## Slide 64: Neural Network Family Map

| Network Type      | Best For                          |
| ----------------- | --------------------------------- |
| ANN / Feedforward | Tabular data                      |
| CNN               | Images                            |
| RNN               | Sequences                         |
| LSTM / GRU        | Long sequences                    |
| Transformer       | Text and GenAI                    |
| Autoencoder       | Compression and anomaly detection |
| GAN               | Data generation                   |
| GNN               | Graph data                        |

---

## Slide 65: ANN / Feedforward Neural Network

ANN is the basic neural network.

Flow:

Input → Hidden Layers → Output

Used for:

* Tabular classification
* Tabular regression
* Basic prediction tasks

---

## Slide 66: ANN Example

Student result prediction:

Inputs:

Study Hours, Attendance, Previous Score

Output:

Pass probability

ANN can learn nonlinear combinations of features.

---

## Slide 67: CNN — Convolutional Neural Network

CNN is mainly used for images.

Examples:

* Cat vs Dog
* Face recognition
* Medical scan classification
* Object detection

---

## Slide 68: How CNN Works

CNN learns spatial patterns.

Image learning flow:

Edges → Shapes → Object Parts → Full Object

Example:

Edges → Eyes/Ears → Face → Cat

---

## Slide 69: Why CNN for Images?

Images have spatial structure.

Nearby pixels are related.

CNN uses filters to detect local patterns.

This makes CNN powerful for image data.

---

## Slide 70: RNN — Recurrent Neural Network

RNN is used for sequence data.

Examples:

* Text
* Time series
* Speech
* Sensor data

RNN processes data step by step.

---

## Slide 71: RNN Example

Sentence:

“I loved the movie because it was amazing.”

The meaning of later words depends on earlier words.

RNN tries to remember previous information.

---

## Slide 72: LSTM and GRU

LSTM and GRU are improved RNNs.

They handle longer memory better.

Used for:

* Long text
* Speech
* Time series forecasting
* Sequence prediction

---

## Slide 73: Why LSTM / GRU?

Basic RNN forgets long-term context.

Example:

“The movie started slowly, but after the interval it became excellent.”

The model must remember both early and later parts.

LSTM / GRU help with this.

---

## Slide 74: Transformer

Transformer is the foundation of modern GenAI.

Used for:

* Chatbots
* Translation
* Summarization
* Question answering
* Code generation

---

## Slide 75: Attention Mechanism

Transformer uses attention.

Attention means:

The model learns which words should focus on which other words.

Example:

“The bank approved the loan because it had strong documents.”

The model learns what “it” refers to.

---

## Slide 76: Why Transformers Are Powerful

Transformers are powerful because they:

* Understand context well
* Process long text better
* Train efficiently at scale
* Power large language models

---

## Slide 77: Autoencoder

Autoencoder learns to compress and reconstruct data.

Structure:

Input → Compressed Representation → Reconstructed Output

Used for:

* Dimensionality reduction
* Noise removal
* Anomaly detection

---

## Slide 78: Autoencoder Example

Normal transaction:

Reconstructed well.

Fraud-like unusual transaction:

Reconstruction error is high.

High reconstruction error may indicate anomaly.

---

## Slide 79: GAN — Generative Adversarial Network

GAN is used to generate new data.

It has two parts:

| Part          | Role                 |
| ------------- | -------------------- |
| Generator     | Creates fake data    |
| Discriminator | Detects fake vs real |

They compete and improve.

---

## Slide 80: GAN Example

Generator creates a fake face image.

Discriminator checks:

Real or fake?

Over time:

Generator becomes better at creating realistic images.

---

## Slide 81: GNN — Graph Neural Network

GNN is used for graph data.

Graph data has nodes and relationships.

Examples:

* Social networks
* Fraud networks
* Recommendation systems
* Molecules
* Knowledge graphs

---

## Slide 82: GNN Example

Fraud detection network:

User → Device → Transaction → Merchant

GNN learns from relationships.

Suspicious connections may reveal fraud patterns.

---

## Slide 83: Section Divider

# Part 8

## ML vs DL Decision Guide

---

## Slide 84: ML vs DL Comparison

| Point               | Classical ML | Deep Learning              |
| ------------------- | ------------ | -------------------------- |
| Data type           | Tabular      | Images, text, audio, video |
| Feature engineering | Manual       | Automatic                  |
| Data required       | Less         | More                       |
| Compute required    | Lower        | Higher                     |
| Interpretability    | Better       | Lower                      |
| Training time       | Faster       | Slower                     |

---

## Slide 85: When to Use Classical ML

Use classical ML when:

* Data is structured
* Dataset is small or medium
* Explanation is important
* Training must be fast
* Business needs clear feature impact

Example:

Loan approval with customer table data.

---

## Slide 86: When to Use Deep Learning

Use Deep Learning when:

* Data is raw and complex
* Images, text, audio, or video are involved
* Large data is available
* Feature learning is needed
* Highest performance matters

Example:

Face recognition or language translation.

---

## Slide 87: Practical Decision Table

| Problem                         | Better Starting Approach |
| ------------------------------- | ------------------------ |
| Student score prediction        | Classical ML             |
| Loan default prediction         | Classical ML             |
| Cat vs Dog image classification | Deep Learning            |
| Speech recognition              | Deep Learning            |
| Customer churn table            | Classical ML             |
| Chatbot                         | Deep Learning            |

---

## Slide 88: Final Summary

Classical ML is strong for structured data.

Deep Learning is strong for raw complex data.

Neural networks learn features automatically.

Different neural networks solve different data problems.

---

## Slide 89: Final Takeaway

Classical ML asks:

Can we learn from prepared features?

Deep Learning asks:

Can the model learn useful features by itself?

The right model depends on:

Data type, data size, accuracy need, compute, and explainability.

---

## Slide 90: Next Step

# Deep Learning Hands-on

Suggested next hands-on:

Build a simple neural network for:

Student pass/fail prediction

Then compare:

Logistic Regression vs Neural Network
