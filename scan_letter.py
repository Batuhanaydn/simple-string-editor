class ScanLetter:
    def scan_letter(string, letter):
        result = 0
        for i in string:
            if i == letter:
                result += 1
        return result

# print(ScanLetter.scan_letter('aaaaaaadsajkdlka', 'a'))