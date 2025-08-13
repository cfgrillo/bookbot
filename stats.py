def get_num_words(book_text):
    return len(book_text.split())

def get_num_characters(book_text):
    result = {}
    for character in book_text:
        char = character.lower()
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result