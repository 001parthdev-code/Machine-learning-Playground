from main import build_corpus, build_bigram, build_trigram, predict_next


if __name__ == "__main__":
    corpus = build_corpus()
    bigram = build_bigram(corpus)
    trigram = build_trigram(corpus)

    while True:
        text = input("Enter text (or quit):" ).strip()
        if text.lower() == "quit":
            break

        result = predict_next(text,trigram,bigram)
        print("Next character:", result)

