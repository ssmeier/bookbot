import sys
from stats import get_num_words
from stats import get_letter_count
from stats import sorted_letter_dict
book_path = None

def get_input():
    input = sys.argv
    if len(input) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        return sys.argv[1]
        
def get_book_text (path_to_book):
    with open(path_to_book) as book:
        book_text = book.read()
    return book_text

def main():
    book_path = get_input()
    print(book_path)
    print('============ BOOKBOT ============')
    print('Analyzing book found at '+ book_path + '...')
    print('----------- Word Count ----------')
    print(get_num_words(get_book_text(book_path)))
    print('--------- Character Count -------')
    letter_dict = (get_letter_count(get_book_text(book_path))).items()
    sorted_letter_dict(letter_dict)

main()