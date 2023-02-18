import re
class Word:
    def word_counter(string):
        a = re.findall('\w+', string)
        return len(a)
