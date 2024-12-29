def main():
    book_path = "books/frankenstein.txt"
    text = read_book(book_path)
    words = num_of_words(text)
    charDict = count_characters(text)
    print(charDict)


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
        charCount[character] = charCount.get(character, 0) + 1

    return charCount


main()
