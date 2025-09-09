def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    result = {}
    for char in text:
        char = char.lower()
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result


def sort_character_counts(character_counts):
    sorted_characters = sorted(
        (
            (char, count)
            for char, count in character_counts.items()
            if char.isalnum()
        ),
        key=lambda item: item[1],
        reverse=True
    )
    return sorted_characters
