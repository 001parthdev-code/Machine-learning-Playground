from main import build_corpus, build_bigram, build_trigram, predict_next

corpus = build_corpus()
bigram = build_bigram(corpus)
trigram = build_trigram(corpus)

print("he →", predict_next("he", trigram, bigram))
print("ha →", predict_next("ha", trigram, bigram))
print("al →", predict_next("al", trigram, bigram))
print("h  →", predict_next("h", trigram, bigram))
print("e  →", predict_next("e", trigram, bigram))
print("ll →", predict_next("ll", trigram, bigram))
