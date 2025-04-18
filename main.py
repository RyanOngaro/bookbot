from stats import word_count
from stats import char_count

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    raw_text = get_book_text(book_path)  
    count = word_count(raw_text)
    print(f"{count} words found in the document")

main()
