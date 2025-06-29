from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
        return file_content

def main():
    # initialize empty book path
    book_path = ""

    # check that a single argument exists
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    if len(sys.argv) == 2:
        book_path = sys.argv[1]
    
    # get all the stats 
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    character_count = get_character_count(book_text)
    sorted_list = get_sorted_list(character_count)

    # pretty report of stats
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_info in sorted_list:
        if char_info["char"].isalpha():
            print(f"{char_info["char"]}: {char_info["num"]}")
    print("============= END ===============")


main()