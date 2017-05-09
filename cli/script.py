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


url = "http://tratu.coviet.vn/hoc-tieng-anh/tu-dien/lac-viet/V-V/%s.html"
import urllib


def find_word_type():
    file = open('data/words.txt', 'r')
    raw_data = file.read()
    file.close()
    counter = 0
    for word in raw_data.split('\n'):
        counter += 1
        if counter < 3240:
            continue
        if counter > 3251:
            break
        print(urllib.quote(word))


find_word_type()
