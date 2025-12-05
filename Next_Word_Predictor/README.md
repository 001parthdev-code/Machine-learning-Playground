# Next Character Predictor (Bigram + Trigram Backoff Model)

A simple yet powerful **next-character language model** built from scratch using **bigrams, trigrams, and backoff logic**.
This project is part of my ML playground where I build foundational NLP concepts from zero — the same principles that scale up to RNNs, LSTMs, and Transformers.

---

## 🚀 What This Project Does

Given some text input, the model predicts the **most likely next character** using:

1. **Trigram Model**
   Uses the last *two characters* to predict the next one.

2. **Bigram Model**
   If trigram information is missing, fall back and use the last *one character*.

3. **Backoff Logic**
   A classical NLP approach used before neural networks became dominant.

---

## 🧠 Why This Matters

This project is not “just a toy.”
You are building the **core idea of language modeling**:

> **Use previous context → predict next token.**

This technique was used in:

* Early Google Search autocomplete
* Early speech recognition
* Statistical machine translation
* Pre-neural NLP systems

Your model is the ancestor of GPT-style models, just much smaller.

---

## 📦 Dataset (Corpus)

Currently using a small word list:

```python
corpus = ["Hello", "Hi", "Halloween"]
```

You can extend this list with any text—sentences, paragraphs, datasets, etc.

---

## 🧩 How It Works

### 🔹 Bigram Model

Counts how often each character is followed by another:

```
'h' → {'e': 2, 'i': 1}
'e' → {'l': 1}
'l' → {'l': 1, 'o': 1}
```

### 🔹 Trigram Model

Counts how often pairs of characters `(c1, c2)` are followed by a third character:

```
('h','e') → {'l': 1}
('a','l') → {'l': 2}
('l','l') → {'o': 2}
```

### 🔹 Backoff Prediction Flow

```
if last two chars exist in trigram → use trigram
else if last char exists in bigram → use bigram
else → return None
```

This mirrors classical NLP language modeling.

---

## 🧪 Example Outputs

Given the corpus, predictions look like:

```
Input: "he" → Output: "l"
Input: "h"  → Output: "e"
Input: "al" → Output: "l"
```

---

## 📁 Project Structure

```
next_character_model/
│
├── main.py   # Bigram + Trigram model logic
└── run.py    # Runs predictions using imported functions
```

`main.py` does not execute anything automatically — it only defines functions.
`run.py` is where you call the model and test outputs.

---

## ▶️ Usage

Run:

```bash
python run.py
```

---

## 🛠 Next Steps (Future Work)

* Add **probability sampling** (instead of always choosing the most common next char)
* Build a **Markov Chain text generator**
* Transition to **RNN** → **LSTM** → **Transformer** models
