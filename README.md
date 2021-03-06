# Wixarika Corpora
## Wixarika language corpora.

At the moment this corpora is in his eary stage, and contins 3 files:
- *segcorpus.wixes* high quality paired corpus with , with Wixarika word segmentation.
- *corpora.wixes* Wixarika - Spanish paired corpus
- *social.wix* Social networks mined wixarika text colection
- *mixed.txt* Social networks mined text that cointains wixarika, spanish and other languages in the same phrase.
- *dictionary.wixes* Wixarika-spanish vocabulary

This work is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.
https://creativecommons.org/licenses/by-nc/4.0/

## Large Corpus

An aditional file *largecorpus.wixes* is a translation form many Grimm and Anderssen stories in Public Domain to Spanish. This work was donde by Dionio Carrillo Gonzáles (dionico94 [-at-] gmail . com) in 2016. This file is licensed by Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) https://creativecommons.org/licenses/by-nc-sa/4.0/ . 

Derivates from this files are:

- *largecorpus2.wixes* Corpus with only unique phrases, with 8967 paired phrases.
- *testset.wixes* Test set with 1000 random chosen lines from largecorpora2.wixarika
- *trainset.wixes* Training set with 7967 unique phrases. 

## Tools

- *sept.py*  Separates training set from testing set, and reduce the corpus to unique lines. This script is GPL 3+

## Citation

If you found this information usfull for your academic research please acknowledge its use with a citation:

Mager, M., Carrillo, D., & Meza, I. (2018). Probabilistic Finite-State morphological segmenter for Wixarika (huichol) language. Journal of Intelligent & Fuzzy Systems, 34(5), 3081-3087.

```
@article{mager2018probabilistic,
  title={Probabilistic Finite-State morphological segmenter for Wixarika (huichol) language},
  author={Mager, Manuel and Carrillo, Di{\'o}nico and Meza, Ivan},
  journal={Journal of Intelligent \& Fuzzy Systems},
  volume={34},
  number={5},
  pages={3081--3087},
  year={2018},
  publisher={IOS Press}
}
```

