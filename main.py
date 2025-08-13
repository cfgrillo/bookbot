from stats import get_num_words
from stats import get_num_characters

def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(book_text)
    num_characters = get_num_characters(book_text)
    return num_characters

print(main())