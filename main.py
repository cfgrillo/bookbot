from stats import (
    get_num_words,
    sort_characters
)

filepath = "books/frankenstein.txt"

def main():
    book_text = get_book_text(filepath)
    num_characters_sorted = sort_characters(book_text)
    total_words = get_num_words(book_text)
    print_report(filepath, total_words, num_characters_sorted)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def print_report(filepath, total_words, num_characters_sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count ------")
    for i in num_characters_sorted:
        if not i["char"].isalpha():
            continue
        print(f"{i['char']}: {i['num']}")
    print("============= END ===============")

main()