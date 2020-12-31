# CYKParser
Implementation of a Probabilistic CYK Parser 
Developed in context of NYU Graduate Natural Language Processing Course

-We wish to parse sentences given specific grammar rules and their production
probabilities over a corpus 

-Using bottom up dynamic programming, more specifically the CYK Parsing Algorithm
we can generate the most likely parse tree

![Alt text](ParseTreeExample.JPG)

 cykparser.py   : implementation of classes for grammar rules and Probabalistic Context Free Grammers (PCFG)
eval.py        : calls cykparser methods and generates most likely parse tree for given datasets
data           : contains grammar rules with probabilities for arithmetic dataset and wall street dataset
