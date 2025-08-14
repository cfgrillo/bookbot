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

def sort_key(item):
    return item["num"]

def sort_characters(book_text):
    character_count = get_num_characters(book_text)
    dictionaries = [{"char": k, "num": v} for k,v in character_count.items()]
    dictionaries.sort(reverse=True, key=sort_key)
    return dictionaries
