def main():
    book_path = "books/frankenstein.txt"
    text = read_book(book_path)
    words = num_of_words(text)
    charDict = count_characters(text)
    sorted_list = chars_dict_to_sorted_list(charDict)

    print("--- Begin report of books/frankenstein.txt ---")
    print(words, "words found in the document \n")

    for item in sorted_list:
        print(f"The '{item['char']}' character was found {item['num']} times")


def read_book(book):
    with open(book) as f:
        return f.read()


def num_of_words(text):
    words = 0
    words = text.split()
    return len(words)


def count_characters(text):
    charCount = {}
    newText = text.lower()
    for character in newText:
        if character.isalpha():
            charCount[character] = charCount.get(character, 0) + 1

    return charCount


def sort_on(dict):
    return dict["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()
