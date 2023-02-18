from collections import Counter

class Frequent:
    def most_frequent_character(string):
        counter = Counter(string)
        most_letter = counter.most_common(5)
        return most_letter


# print(Frequent.most_frequent_character('dsjakldasadasdadsaddd'))