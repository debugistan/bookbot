import sys
from stats import count_words, count_characters, sort_character_counts


def get_book_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    word_count = count_words(book_text)
    character_counts = count_characters(book_text)
    sorted_character_counts = sort_character_counts(character_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char, count in sorted_character_counts:
        print(f"{char}: {count}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
