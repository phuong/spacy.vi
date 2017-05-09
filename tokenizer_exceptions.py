# encoding: utf8
from __future__ import unicode_literals

from ..symbols import *
from ..language_data import PRON_LEMMA


TOKENIZER_EXCEPTIONS = {
    "ko": [
        {ORTH: "ko", LEMMA: "không"}
    ],
    "đ/c": [
        {ORTH: "d/c", LEMMA: "địa chỉ"},
        {ORTH: "đ/c", LEMMA: "địa chỉ"}
    ],
    "cty": [
        {ORTH: "cty", LEMMA: "công ty"},
    ]
}

orth_char = 'aàảãáạăằẳẵắặâầẩẫấậbcdđeèẻẽéẹêềểễếệfghiìỉĩíịjklmnoòỏõóọôồổỗốộơờởỡớợpqrstuùủũúụưừửữứựvwxyỳỷỹýỵz'
ORTH_ONLY = []
for char in orth_char:
    ORTH_ONLY.append('%s.' % char)
