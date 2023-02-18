import re
class ScanWord:
    def scan_word(string, word):
        string = string.lower()
        result = 0
        a = re.findall('\w+', string)
        for i in a:
            if i == word:
                result += 1
        return result

print(ScanWord.scan_word('ahmet ali ayse, ayse', 'ayse'))