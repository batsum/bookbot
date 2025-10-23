import sys
from stats import get_num_words,get_num_chars, sort_list, sort_on

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    path_to_book = sys.argv[1]
    text = get_book_text(path_to_book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    word_count = get_num_words(text)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    char_counts = get_num_chars(text)
  

    char_list = sort_list(char_counts)
    for dic in char_list:
        print(dic["char"]+": "+str(dic["num"]))
    print("============= END ===============")

main()

