# encoding: utf8
from __future__ import unicode_literals

f = open('data/stop_words.txt', 'r')
data = f.read()
f.close()

delimiter = '\n'.encode('utf-8')

STOP_WORDS = set(data.split(delimiter))
