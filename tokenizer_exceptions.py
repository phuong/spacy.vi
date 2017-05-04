# encoding: utf8
from __future__ import unicode_literals

from ..symbols import *
from ..language_data import PRON_LEMMA


TOKENIZER_EXCEPTIONS = {
    "ko": [
        {ORTH: "ko", LEMMA: "không"}
    ]
}

orth_char = 'aàảãáạăằẳẵắặâầẩẫấậbcdđeèẻẽéẹêềểễếệfghiìỉĩíịjklmnoòỏõóọôồổỗốộơờởỡớợpqrstuùủũúụưừửữứựvwxyỳỷỹýỵz'
ORTH_ONLY = []
for char in orth_char:
    ORTH_ONLY.append('%s.' % char)