class RemoveNewLine:
    def remove_new_line(string):
        result = ""
        for i in string:
            if i == '\n':
                pass
            else:
                result += i
        return result

# print(RemoveNewLine.remove_new_line('''Merhaba
# Ben
# Batuhan
# Aydın'''))