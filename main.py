from stats import word_count
from stats import char_count
from stats import sorted_char_count

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    raw_text = get_book_text(book_path)  
    wcount = word_count(raw_text)
    ccount = char_count(raw_text)
    s_ccount = sorted_char_count(ccount)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {wcount} total words")
    print("--------- Character Count -------")

    for c in s_ccount:
        print(f"{c["Letter"]}: {c["Number"]}")

    print("============= END ===============")
    

main()
