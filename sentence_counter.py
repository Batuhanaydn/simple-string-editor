import re
class Sentence:
    def sentence_counter(string):
        result = 0
        a = re.split(r'[.!?]+', string)
        for _ in a:
            result += 1
        return result
