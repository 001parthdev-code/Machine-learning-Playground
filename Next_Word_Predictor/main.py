from collections import defaultdict, Counter

#This is the dataset 
corpus = ["Hello", "Hi", "Halloween"]
corpus = [word.lower() for word in corpus]

counts = defaultdict(Counter)
for word in corpus:
    for a,b in zip(word, word[1:]):
        counts[a][b] +=1

def predict_next(char,counts):
    char = char.lower() #convert input to lowercase 
    if char not in counts:
        return None
    return counts[char].most_common(1)[0][0]

print(predict_next('He', counts))