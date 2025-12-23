def get_num_words (input_text):
    wordlist = input_text.split()
    wordcount = len(wordlist)
    return "Found "+ str(wordcount) +" total words"