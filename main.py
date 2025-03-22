from stats import sorted_charactor_count,get_word_count
import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def print_report(path):
    raw_text = get_book_text(path)
    total_words = get_word_count(raw_text)
    char_list = sorted_charactor_count(raw_text)



    print("============ BOOKBOT ============")
    print("Analyzing book found at", path, "...")
    print("----------- Word Count ----------")
    print("Found",total_words,"total words")
    print("--------- Character Count -------")
    for item in char_list:
        if(item["char"].isalpha()):
                print(item["char"] + ":" , item["count"])
                

def main():
    if(len(sys.argv)<2):
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)

    print_report(sys.argv[1])


main()
