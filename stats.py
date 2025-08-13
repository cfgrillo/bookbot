def get_num_words(book_text):
    return len(book_text.split())

def get_num_characters(book_text):
    result = {}
    for character in book_text:
        if character in result:
            result[character] += 1
        else:
            result[character] = 1
    return result