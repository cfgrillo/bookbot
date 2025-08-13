def get_book_text(filepath):
    with open(filepath) as f:
        f = f.read()
    return f

def main():
    book_text = get_book_text("books/frankenstein.txt")
    return book_text

main()