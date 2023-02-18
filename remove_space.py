class RemoveSpace:
    def remove_space(string):
        result = ""
        for i in string:
            if i == " ":
                pass
            else:
                result += i
        return result

# print(RemoveSpace.remove_space('Merhaba ben batuhan aydın'))