from stats import get_num_words
from stats import get_letter_count
from stats import sorted_letter_dict

def get_book_text (path_to_book):
    with open(path_to_book) as book:
        book_text = book.read()
    return book_text

def main():
    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
    print('----------- Word Count ----------')
    print(get_num_words(get_book_text("books/frankenstein.txt")))
    print('--------- Character Count -------')
    letter_dict = (get_letter_count(get_book_text("books/frankenstein.txt"))).items()
    sorted_letter_dict(letter_dict)

main()