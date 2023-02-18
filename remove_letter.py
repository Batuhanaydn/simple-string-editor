class RemoveLetter:
    def remove_letter(string, letter):
        result = ""
        if len(letter) != 1:
            return "Please enter a letter!"
        else:
            for i in string:
                if i == letter:
                    pass
                else:
                    result += i
        return result
print(RemoveLetter.remove_letter('ahmet mehmet', 'm'))