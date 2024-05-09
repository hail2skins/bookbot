from collections import Counter

def main():
    """
    Read the text from the file at the given path and print a report of the
    number of words and the number of times each letter appears in the text.
    """
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    letter_count = get_letter_count(text)
    chars_sorted_list = chars_dict_to_sorted_list(letter_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_book_text(path):
    """
    Read the text from the file at the given path and return it as a string.
    """
    with open(path, encoding='utf-8') as f:
        return f.read()
    

def get_word_count(text):
    """
    Count the number of words in the text. Words are separated by spaces.
    """
    words = text.split()
    return len(words)

def get_letter_count(text):
    """
    Count the number of each letter in the text. Return a dictionary
    with the letter as the key and the count as the value. Convert each letter
    to lowercase before counting.
    """
    # lowered_text = text.lower()
    # letter_count = {}
    # # For each letter in lowered_text, count the number of times it appears.
    # # If letter doesn't exist in the dictionary add it with a count of 1
    # # If letter does exist, increment the count by 1
    # for letter in lowered_text:
    #     if letter in letter_count:
    #         letter_count[letter] += 1
    #     else:
    #         letter_count[letter] = 1
    # return letter_count
    return Counter(text.lower()) # This is a more concise way to do the same thing as above.

def sort_on(d):
    """
    Sort a dictionary by the values in descending order.
    """
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    """
    Convert a dictionary of characters and their counts to a list of dictionaries.
    Each dictionary in the list should have two keys: "char" and "num".
    """
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
       
main()
