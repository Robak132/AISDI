from Testing import Testing


def dictify(string):
    temp_dict = {}
    for value, letter in enumerate(string[::-1]):
        if letter not in temp_dict.keys():
            temp_dict.update({letter: value})
    return dict


def special_algorithm(string, text):
    p = 0
    list_of_pos = []
    for i in range(len(text)):
        if string[p] == text[i]:
            p += 1
            if p == len(string):
                list_of_pos.append(i - len(string) + 1)
                p = 0
        else:
            p = 0
    return list_of_pos


def make_words_and_text(_file, n):
    with open(_file, "r", encoding="utf-8") as file:
        lines = file.readlines()
        plain_text = ""
        for line in lines:
            if line.strip() != "":
                plain_text = plain_text + line.strip() + " "
        words = plain_text.split(" ")[:n]
        return words, plain_text


if __name__ == "__main__":
    words, text = make_words_and_text("Wzorcowansko\\pan-tadeusz.txt", 100)
    for word in words:
        special_algorithm(word, text)
    # d = dictify("halpha")
    # print(d.keys())
    # print(d.values())
