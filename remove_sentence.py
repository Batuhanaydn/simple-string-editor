import re
class RemoveSentence:
    def remove_sentence(string, sentence):
        result = ""
        string = string.lower()
        sentence = sentence.lower()
        a = re.split(r'[.!?]+', string)
        for i in a:
            if i == sentence:
                pass
            else:
                result += i

        return result

print(RemoveSentence.remove_sentence('Merhaba. Ben batuhan aydın.', ' ben batuhan aydın'))