def count_words_in(string):
    return len(string.split())


def generate_histogram_from(string):
    from collections import Counter
    return Counter(string.lower())


def generate_report_from(file_contents):
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{count_words_in(file_contents)} words found in the document\n')

    for char, count in sorted(generate_histogram_from(file_contents).items(), key=lambda x: x[1], reverse=True):
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")


with open('books/frankenstein.txt') as f:
    file_contents = f.read()
    generate_report_from(file_contents)
