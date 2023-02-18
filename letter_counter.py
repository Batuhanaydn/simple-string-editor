import re
class Letter:
    def letter_counter(string):
        result = 0
        a = re.findall(' ', string)
        space_number = len(a)
        for i in string:
            for j in i:
                result += 1
        return result - space_number
