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

def sort_on(dict):
    return dict["Number"]

def sorted_char_count(char_dict):
    char_count_list = []
    for letter in char_dict:
        if letter.isalpha():
            number = char_dict[letter]
            char_count_list.append({"Letter" : letter, "Number" : number})
    char_count_list.sort(reverse=True, key=sort_on)
    return char_count_list

