from __future__ import absolute_import
from ..data import from_file
from ._lemma_rules import ADJECTIVE_RULES, NOUN_RULES, VERB_RULES, PUNCT_RULES

ADVERBS = from_file('data/ADV.txt')
VERBS = from_file('data/VERB.txt')
NOUNS = from_file('data/NOUN.txt')
ADJECTIVES = from_file('data/ADJ.txt')

RULES = 'LOAD RULES'
EXC = 'LOAD EXC'

INDEX = {
    "adj": ADJECTIVES,
    "adv": ADVERBS,
    "noun": NOUNS,
    "verb": VERBS
}

RULES = {
    "adj": ADJECTIVE_RULES,
    "noun": NOUN_RULES,
    "verb": VERB_RULES,
    "punct": PUNCT_RULES
}
