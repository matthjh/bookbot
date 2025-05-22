def get_num_words(text):
    num_words = len(text.split())
    return(num_words)
    #print(f"{num_words} words found in the document")

def get_char_count(text):
    low_split = text.lower()
    char_counts = {}
    for word in low_split:
        char_counts[word] = char_counts.get(word, 0) + 1
    return(char_counts)

def sort_on(dict):
    return dict["num"]

def get_text_sorted(text):
    low_split = text.lower()
    char_counts = {}
    char_sorted = []
    for char in low_split:
        char_counts[char] = char_counts.get(char, 0) + 1
    for char, count in char_counts.items():
        if char.isalpha():
            char_sorted.append({"char": char, "num": count})
    char_sorted.sort(reverse=True, key=sort_on)
    return(char_sorted)

if __name__ == "__main__":
    #print(get_char_count("Hello there!"))
    print(get_text_sorted("books/frankenstein.txt"))