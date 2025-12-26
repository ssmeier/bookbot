def get_num_words (input_text):
    wordlist = input_text.split()
    wordcount = len(wordlist)
    return "Found "+ str(wordcount) +" total words"

def get_letter_count (input_text):
    letter_dict = {}
    for char in input_text:
        char = char.lower()
        if char in letter_dict:
            letter_dict[char] = (letter_dict.get(char) + 1)
        else:
            letter_dict[char] = 1

    return letter_dict

def sort_on_count(item):
    return item["num"]

def sorted_letter_dict (input_dict):
    sorted_list = []
    for item in input_dict:
        entry = {"char": item[0], "num": item[1]}
        sorted_list.append(entry)
    sorted_list.sort(key=sort_on_count, reverse=True)
    for item in sorted_list:
        print(item["char"] + ": " + str(item["num"]))
    return