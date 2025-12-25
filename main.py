from stats import get_num_words
from stats import get_letter_count

def get_book_text (path_to_book):
    with open(path_to_book) as book:
        book_text = book.read()
    return book_text

def main():
    print(get_num_words(get_book_text("books/frankenstein.txt")))
    print(get_letter_count(get_book_text("books/frankenstein.txt")))
main()