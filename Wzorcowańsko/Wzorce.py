def dictify(string):
    temp_dict = {}
    for value, letter in enumerate(string[::-1]):
        if letter not in temp_dict.keys():
            temp_dict.update({letter: value})
    return dict

d = dictify("halpha")
print(d.keys())
print(d.values())