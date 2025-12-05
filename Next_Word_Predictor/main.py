from collections import defaultdict, Counter

#-------------------
#   DATASET(corpus)
#-------------------

def build_corpus():
    corpus = ["Hello", "Hi", "Halloween"]
    return [word.lower() for word in corpus]


# -------------------------------------
# 2️⃣ Build BIGRAM model
#    counts_bigram[a][b] = freq of b after a
# -------------------------------------

def build_bigram(corpus):
    counts_bigram = defaultdict(Counter)
    for word in corpus:
        for a, b in zip(word, word[1:]):
            counts_bigram[a][b] += 1
    return counts_bigram



# -------------------------------------
# 3️⃣ Build TRIGRAM model
#    counts_trigram[(c1, c2)][c3] = freq of c3 after (c1, c2)
# -------------------------------------

def build_trigram(corpus):
    counts_trigram = defaultdict(Counter)
    for word in corpus:
        for c1, c2, c3 in zip(word, word[1:], word[2:]):
            counts_trigram[(c1, c2)][c3] += 1
    return counts_trigram
    

# -------------------------------------
# 4️⃣ Predict next character (BACKOFF):
#    Try trigram → bigram → fallback
# -------------------------------------

def predict_next(text, trigram, bigram):
    text = text.lower()

    # Try trigrams
    if len(text) >= 2:
        key = (text[-2], text[-1])
        if key in trigram:
            return trigram[key].most_common(1)[0][0]

    # Try bigrams
    if len(text) >= 1:
        key = text[-1]
        if key in bigram:
            return bigram[key].most_common(1)[0][0]
    
    #no information given
    return None



if __name__ == "__main__":
    # quick local test
    corpus = build_corpus()
    bigram = build_bigram(corpus)
    trigram = build_trigram(corpus)


if __name__ == "__main__":
    # quick local test
    corpus = build_corpus()
    bigram = build_bigram(corpus)
    trigram = build_trigram(corpus)

    print("he →", predict_next("he", trigram, bigram))
    print("ha →", predict_next("ha", trigram, bigram))
    print("al →", predict_next("al", trigram, bigram))
    print("h  →", predict_next("h", trigram, bigram))
    print("e  →", predict_next("e", trigram, bigram))
    print("ll →", predict_next("ll", trigram, bigram))

