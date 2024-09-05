def main():
    book_path = "books/frankenstein.txt"
    report = generate_report(book_path)
    print(report)

def generate_report(path):
    text = read_book_text(path)
    words_count = count_words(text)
    chars_count = count_characters(text)
    sorted_chars_count = sort_characters_by_count(chars_count)

    report = f"--- Begin report of {path} ---\n"
    report += f"{words_count} words found in the document\n\n"

    for char_info in sorted_chars_count:
        if not char_info["char"].isalpha():
            continue
        report += f"The '{char_info['char']}' character was found {char_info['count']} times\n"

    report += "--- End report ---"
    return report

def count_words(text):
    return len(text.split())

def sort_by_count(char_info):
    return char_info["count"]

def sort_characters_by_count(chars_count):
    sorted_chars = []
    for char, count in chars_count.items():
        sorted_chars.append({"char": char, "count": count})
    sorted_chars.sort(key=sort_by_count, reverse=True)
    return sorted_chars

def count_characters(text):
    chars_count = {}
    for char in text:
        char_lower = char.lower()
        if char_lower in chars_count:
            chars_count[char_lower] += 1
        else:
            chars_count[char_lower] = 1
    return chars_count

def read_book_text(path):
    with open(path) as file:
        return file.read()

main()