from Testing import Testing


def dictify(string):
    temp_dict = {}
    for value, letter in enumerate(string[::-1]):
        if letter not in temp_dict.keys():
            temp_dict.update({letter: value})
    return temp_dict


def boilerMur(find, text):
    dicty = dictify(find)
    print(dicty)
    F = len(text)
    T = len(find)
    ans_tab = []
    if F==0 or T==0:
        return ans_tab
    index = 0
    while index <= F-T:
        j = T-1
        while j>=0 and find[j] == text[index+j]:
            j -= 1
        if (j == -1): 
            ans_tab.append(index)
            index += 1
        else: 
            if text[index+j] in dicty.keys():
                index += max(dicty[text[index+j]], 1)
            else: index += j+1   
    return ans_tab


def testBoilerMur():
    pure_thruth = []
    pure_thruth.append(boilerMur("cdeca", "cdeca") == [0])
    pure_thruth.append(boilerMur("cdeca", "cdec") == [])
    pure_thruth.append(boilerMur("cdeca", "bcdecab") == [1])
    pure_thruth.append(boilerMur("", "") == [])
    pure_thruth.append(boilerMur("hmm", "") == [])
    pure_thruth.append(boilerMur("", "hmm") == [])
    pure_thruth.append(boilerMur( "decde","abcdecdecde" ) == [3,6])
    pure_thruth.append(boilerMur( "aaa","aaaaaaaaaaa" ) == [0,1,2,3,4,5,6,7,8])
    print(pure_thruth)


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
