import re
class RemoveWord:
    def remove_word(string, word):
        result = ""
        string = string.lower()
        a = re.findall('\w+', string)
        for i in a:
            if i == word:
                pass
            else:
                result += i + " "
        return result