# -*- coding: utf-8 -*-

def clean_vi_dictionary():
    write = open('data/words2.txt', 'w')

    file = open('data/words.txt', 'r')
    raw_data = file.read()
    file.close()
    section = []
    section_length = 0
    count = 0
    words = []
    for w in raw_data.split('\n'):
        section = w.split()
        section_length = len(section)
        section = section[:section_length - 2]
        word = ' '.join(section)
        if word not in words:
            words.append(word)
            write.write('%s\n' % word)
    write.close()


###########################################################################

SOURCE_URL = "http://tratu.coviet.vn/hoc-tieng-anh/tu-dien/lac-viet/V-V/%s.html"
import urllib
import requests
from lxml import html

NOUN = u'danh từ'
ADJ = u'tính từ'
ADV = u'trạng từ'
VERB = u'động từ'
PRONN = u'đại từ'
CONJ = u'kết từ'
PREP = u'giới từ'

LEMMA = [NOUN, ADJ, ADV, VERB, PRONN, CONJ, PREP]
LEMMAP = {
    NOUN: 'NOUN',
    ADJ: 'ADJ',
    ADV: 'ADV',
    VERB: 'VERB',
    PRONN: 'PRONN',
    CONJ: 'CONJ',
    PREP: 'PREP'
}


def find_type_of_word(word):
    url = SOURCE_URL % urllib.quote(word.encode('utf8'))
    req = requests.get(url)
    tree = html.fromstring(req.content)
    ub = tree.xpath('//div[@class="ub"]')
    for lemma in ub:
        lemma = lemma.text_content().strip()
        if lemma in LEMMA:
            yield LEMMAP[lemma]


def build_word_type_data():
    # file = open('data/words.txt', 'r')
    # raw_data = file.read()
    # file.close()
    raw_data = u"""hoặc|một|nếu|bởi vì"""
    counter = 0

    for word in raw_data.split('|'):
        w = find_type_of_word(word)
        print(word, "=")
        for _w in w:
            print(_w)


build_word_type_data()
