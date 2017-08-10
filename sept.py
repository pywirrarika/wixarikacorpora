#!/bin/bash

# Jesús Mager, 2017, licenced with GPL3+

import random

corpus = open("largecorpus.wixes", "r").read().split("\n")
Ftest = open("testset.wixes", "w")
Ftrain = open("trainset.wixes", "w")
Fnew = open("largecorpus2.wixes", "w")

random.seed(42)
unique_corpus = set(corpus)
print("Total corpus:", str(len(unique_corpus)))
test = set(random.sample(unique_corpus, k=1000))
print("Test set:", str(len(test)))
train = unique_corpus - test
print("Train set:", str(len(train)))

for line in list(test):
    print(line, file=Ftest)

for line in list(train):
    print(line, file=Ftrain)

for line in list(unique_corpus):
    print(line, file=Fnew)
