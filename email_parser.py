#!/usr/bin/python

import nltk
from nltk.stem.snowball import SnowballStemmer
import string


def parseOutText(f):
    """ given an opened email file f, parse out all text below the
        metadata block at the top
        """

    stemmer = SnowballStemmer("english")

    f.seek(0)  ### go back to beginning of file (annoying)
    all_text = f.read()

    ### split off metadata
    content = all_text.split("X-FileName:")
    words = ""
    if len(content) > 1:
        ### remove punctuation
        text_string = content[1].translate(string.maketrans("", ""), string.punctuation)

        ### project part 2: comment out the line below
        ### splits sentence into words
        sentence = nltk.sent_tokenize(text_string)

        stemmedSentence = []
        tokenizedSentence = []

        for word in sentence:
            tokenizedSentence = nltk.word_tokenize(word)

        for word in tokenizedSentence:
            stemmedSentence.append(stemmer.stem(word))

        ### split the text string into individual words, stem each word,
        ### and append the stemmed word to words (make sure there's a single
        ### space between each stemmed word)

        for i in range(0, len(stemmedSentence)):
            if i == 0:
                words = stemmedSentence[i]

            else:
                words = words + " " + stemmedSentence[i]

    return words


def main():
    ff = open("/Users/idaly666/PycharmProjects/nltkTest/sample_data/test_email.txt", "r")
    text = parseOutText(ff)
    print text


if __name__ == '__main__':
    main()

