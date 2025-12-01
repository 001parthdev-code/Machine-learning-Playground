# Next Word Predictor (Bigram Model)

A simple *next-character predictor* in Python that predicts the most likely next character based on a *bigram frequency model*.  

This project is part of my ML playground where I experiment with small AI/ML projects to build intuition and foundational skills.

---

## Features

- Predicts the *next character* given a single character or partial word.
- Uses a *bigram frequency model* (counts how often one character follows another in the corpus).
- Corpus is currently hardcoded but can be easily extended.

---

## Dataset

The corpus is a small list of words:

```python
corpus = ["Hello", "Hi", "Halloween"]