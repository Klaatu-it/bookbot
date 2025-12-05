#prints the count of words in a string
def words_counter(string):
    words_list = string.split()
    counter = 0
    for word in words_list:
        counter += 1
    print (f"Found {counter} total words")
    return counter


def count_characters(string):
    c_set=set()
    for c in string:
        c_set.add(c.lower())
    c_dict = {}
    for ch in c_set:
        counter = 0
        for c in string:
            if c.lower() == ch:
                counter += 1
        c_dict[ch] = counter
    return c_dict


def sort_on(dict):
    return dict["num"]


def sorted_list(dict):
    dict_list = []
    for ch in dict:
        char_dict = {}
        char_dict["char"] = ch
        char_dict["num"] = dict[ch]
        dict_list.append(char_dict)
    dict_list.sort(reverse = True, key = sort_on)
    return dict_list




