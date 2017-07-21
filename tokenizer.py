import nltk
from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")

stringTest = "Runner in the responsiveness slacker and unhighness in the shadows"
sentence = nltk.sent_tokenize(stringTest)


tokenizedSentence = []

for word in sentence:
    tokenizedSentence = nltk.word_tokenize(word)

stemmedSentence = []
count = 0

for word in tokenizedSentence:
    stemmedSentence.append(stemmer.stem(word))

print tokenizedSentence
print stemmedSentence
