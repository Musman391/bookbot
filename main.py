def main():
    book_path = "books/frankenstein.txt"
    text = read_book(book_path)
    words = num_of_words(text)
    count_characters(text)


def read_book(book):
    with open(book) as f:
        return f.read()


def num_of_words(text):
    words = 0
    words = text.split()
    return len(words)


def count_characters(text):
    charCount = {}
    words = text.split()
    for word in words:
        for character in word:
            charCount[character] = charCount.get(character, 0) + 1

    for character in charCount:
        print(character + ":" + charCount[character])


main()
