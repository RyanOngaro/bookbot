def word_count(book_string):
    words = book_string.split()
    return len(words)

def char_count(book_string):
    characters = {}
    chars = list(book_string.lower())
    for char in chars:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters
    ## characters["x"] += 1