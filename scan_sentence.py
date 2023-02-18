import re
class ScanSentence:
    def scan_sentence(string, sentence):
        result = 0
        a = re.split(r'[.!?]+', string)
        for i in a:
            if i == sentence:
                result += 1
        return result

# print(ScanSentence.scan_sentence('ahmetali. ahmetveli. ahmetveli.', ' ahmetveli'))