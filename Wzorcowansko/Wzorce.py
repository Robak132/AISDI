import timeit
from random import choice

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'x', 'y', 'z']


def dictify(string):
    temp_dict = {}
    for value, letter in enumerate(string[::-1]):
        if letter not in temp_dict.keys():
            temp_dict.update({letter: value})
    return temp_dict


def boilerMur(find, text):
    dicty = dictify(find)
    F = len(text)
    T = len(find)
    ans_tab = []
    if F == 0 or T == 0:
        return ans_tab
    index = 0
    while index <= F - T:
        j = T - 1
        while j >= 0 and find[j] == text[index + j]:
            j -= 1
        if (j == -1):
            ans_tab.append(index)
            index += 1
        else:
            if text[index + j] in dicty.keys():
                index += max(dicty[text[index + j]], 1)
            else:
                index += j + 1
    return ans_tab


def testBoilerMur():
    pure_thruth = []
    pure_thruth.append(boilerMur("cdeca", "cdeca") == [0])
    pure_thruth.append(boilerMur("cdeca", "cdec") == [])
    pure_thruth.append(boilerMur("cdeca", "bcdecab") == [1])
    pure_thruth.append(boilerMur("", "") == [])
    pure_thruth.append(boilerMur("hmm", "") == [])
    pure_thruth.append(boilerMur("", "hmm") == [])
    pure_thruth.append(boilerMur("decde", "abcdecdecde") == [3, 6])
    pure_thruth.append(boilerMur("aaa", "aaaaaaaaaaa") == [0, 1, 2, 3, 4, 5, 6, 7, 8])
    print(pure_thruth)


def special_algorithm(string, text):
    len_t = len(text)
    len_s = len(string)
    list_of_pos = []
    if len_s == 0 or len_t == 0 or len_s > len_t:
        return list_of_pos
    for i in range(len_t - len_s + 1):
        if string == text[i:i + len_s]:
            list_of_pos.append(i)
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


def make_tests(function):
    print("pusty jeden lub oba napisy wejściowe")
    print(function("", "cos") == [])
    print(function("cos", "") == [])
    print(function("", "") == [])

    print("napis ‘string’ równy napisowi 'text'")
    print(function("string", "string") == [0])

    print("napis ‘string’ dłuższy od napisu ‘text’")
    print(function("dlugistring", "string") == [])

    print("napis ‘string’ nie występuje w ‘text’")
    print(function("string", "test") == [])

    print("'abc' in 'abcefgrtyabeabccvabc'")
    print(function("abc", "abcefgrtyabeabccvabc") == [0, 12, 17])

    print("'a' in 'aaaaaaaaaaaa'")
    print(function("a", "aaaaaaaaaaaa") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    print("'ma' in 'Mama ma kota'")
    print(function("ma", "Mama ma kota") == [2, 5])


def save_result_to_file(function, namefile):
    with open("Wzorcowansko\\{namefile}", "w+") as newfile:
        n = 201
        dn = 10
        words, text = make_words_and_text("Wzorcowansko\\pan-tadeusz.txt", n)

        string_s = f"from __main__ import {function}\nfrom __main__ import text, words"
        for i in range(0, len(words), dn):
            time = 0
            for j in words[:i]:
                time += timeit.timeit(f"{function}('{j}', text)", string_s, number=1)
            print(i)
            newfile.write(f"{str(time).replace('.', ',')};")


def random_test(amount=1):
    for j in range(amount):
        text = ""
        for i in range(500):
            text += choice(alphabet)
        key = ""
        for i in range(2):
            key += choice(alphabet)

        _naive = special_algorithm(key, text)
        _boilermur = boilerMur(key, text)
        print(_naive == _boilermur)


if __name__ == "__main__":
    # make_tests(special_algorithm)
    # make_tests(boilerMur)
    # random_test(10)

    # save_result_to_file(special_algorithm, "naiwny.txt")
    # save_result_to_file(boilerMur, "boilermur.txt")