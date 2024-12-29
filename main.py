def main():
    book_path = "books/frankenstein.txt"
    text = read_book(book_path)
    words = num_of_words(text)
    print(words)


def read_book(book):
    with open(book) as f:
        return f.read()


def num_of_words(text):
    words = 0
    for word in text.split():
        words += 1

    return words


main()
