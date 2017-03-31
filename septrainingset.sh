#!/bin/bash

# This files describes the method used to separte a training set and a test set
# from largecorpus.wixes. This script should only be run once, so the
# possible tests of translations can be consistent. 

# The size of the test set
testsize=500

# Function to generate true random based on a given seed
get_seeded_random()
{
    seed="$1"
    openssl enc -aes-256-ctr -pass pass:"$seed" -nosalt \
    </dev/zero 2>/dev/null
}

# Generate two subsets of largecorpus.wixes. We take a given size of lines as a test set
# using seed 42. The lest lines will used as the training set. 
sort --random-source=<(get_seeded_random 42) -R largecorpus.wixes | head -n $testsize > testset.wixes
grep -v -x -f testset.wixes largecorpus.wixes > trainset.wixes
