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
# This section is used to build lemma, type of word

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
ART = u'mạo từ'
PROPN = u'danh từ riêng'

LEMMA = [NOUN, ADJ, ADV, VERB, PRONN, CONJ, PREP, ART, PRONN]
LEMMAP = {
    NOUN: 'NOUN',
    ADJ: 'ADJ',
    ADV: 'ADV',
    VERB: 'VERB',
    PRONN: 'PRONN',
    CONJ: 'CONJ',
    PREP: 'PREP',
    ART: 'ART',
    PROPN: 'PROPN'
}


def find_type_of_word(word):
    url = SOURCE_URL % urllib.quote(word)
    req = requests.get(url)
    tree = html.fromstring(req.content)
    ub = tree.xpath('//div[@class="ub"]')
    lemmas = []
    for lemma in ub:
        lemma = lemma.text_content().strip()
        if lemma in LEMMA:
            lemmas.append(LEMMAP[lemma])
    return lemmas

vi_title = u'ÀẢÃÁẠĂẰẲẴẮẶÂẦẤẨẪẬĐÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌỒỐỔỖỘỜỚỞỠỢÙÚỦŨỤỪỨỬỮỰỲÝỶỸỴ'.encode('utf8')

def is_prop_noun(word):
    words = word.split()
    word_length = len(words)
    found = 0
    for w in words:
        if w[0].istitle() or w[0] in vi_title:
            found += 1
    if found == word_length:
        return True
    return word_length > 3 and found >= 2


def normalize_word(word):
    if isinstance(word, str):
        word = unicode(word, 'utf-8')
    word = word.encode('utf8')
    return word


def build_word_type_data():
    file = open('data/words.txt', 'r')
    raw_data = file.read()
    file.close()

    file_lemmas = dict()
    file_prop_noun = open('data/PRONOUN.txt', 'w')
    file_undefined = open('data/undefined.txt', 'w')
    file_lemma = open('data/lemma.txt', 'w')

    def get_file(lemma):
        if lemma not in file_lemmas:
            file_lemmas[lemma] = open('data/%s.txt' % lemma, 'w')
        return file_lemmas[lemma]

    def close_files():
        file_prop_noun.close()
        file_undefined.close()
        file_lemma.close()
        for key, file in file_lemmas.items():
            file.close()

    def proccess_word(word):
        word = normalize_word(word)
        print("Working with %s " % word)
        if is_prop_noun(word):
            file_prop_noun.write('%s\n' % word)
        else:
            lemmas = find_type_of_word(word)
            if lemmas:
                for lemma in lemmas:
                    get_file(lemma).write('%s\n' % word)
                file_lemma.write('%s;%s\n' % (word, ','.join(lemmas)))
            else:
                file_undefined.write('%s\n' % word)

    data = raw_data.split('\n')
    for i in range(2030, 2080):
        word = data[i]
        proccess_word(word)

    close_files()

build_word_type_data()