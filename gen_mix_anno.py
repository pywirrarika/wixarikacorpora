import re

data = open('mixed.txt').read().split('\n')
out = open('mixed_annotated.txt', 'w')


def tokenize(text):
    text = re.sub(r"(?<![\s])([.|,|,\-,\"|:|;|¿|?|¡|!])+", r" \1", text)
    text = re.sub(r"([.|,|,\-,\"|:|;|¿|?|¡|!])+(?<![\s])", r"\1 ", text)
    return text

for sentence, text in zip(range(len(data)), data):
    text = tokenize(text).split()
    for token in text:
        print(sentence, token)
        print(sentence, token, file=out)

    print()

