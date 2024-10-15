def main():
    file_path = "books/frankenstein.txt"
    book_str = read_book(file_path)
    num_words = count_words(book_str)
    char_count_dict = count_unique_characters(book_str)
    char_count_dict_list = dict_2_list(char_count_dict)
    char_count_dict_list.sort(reverse=True, key=sort_on_char_list)

    print(f"--- Begin report of {file_path} ---")
    print(f"{num_words} words found in the document")
    for char in char_count_dict_list:
        if char["character"].isalpha():
            print(f"The {char["character"]} character was found {char["occurences"]} times")
    print("--- End report ---")

def read_book(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def count_words(book_str):
    words = book_str.split()
    return(len(words))

def count_unique_characters(book_str):
    char_dict = {}
    for char in book_str.lower():
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def dict_2_list(dict):
    dict_list = []
    for key in dict:
        value = dict[key]
        dict_list.append({"character": key, "occurences": dict[key]})
    return dict_list

def sort_on_char_list(char_dict):
    return char_dict["occurences"]

main()