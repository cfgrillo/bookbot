def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def get_num_words(book_text):
    return len(book_text.split(" "))

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(book_text)
    return f"{num_words} words found in the document."

print(main())