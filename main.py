import stats
import sys


def get_book_text(file_path):
    with open(f"{file_path}") as f:
        file_contents = f.read()
    return file_contents

def print_report(file_path, word_count, char_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    for c in char_list:
        print(f"{c['char']}: {c['num']}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    args = sys.argv

    file_path = args[1]
    details = get_book_text(file_path)
    char_count = stats.get_char_count(details)
    word_count = stats.get_num_words(details)
    char_list = stats.get_text_sorted(details)
    #print(char_count)
    print_report(file_path, word_count, char_list)

main()          