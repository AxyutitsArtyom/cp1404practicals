"""
Word Occurrences
Estimate: 20 minutes
Actual:   32 minutes
"""


def main():
    word_to_count = {}
    text = input("Text: ")
    text = text.split()
    text.sort()

    turn_text_into_dictionary(text, word_to_count)

    print_word_count(word_to_count)


def print_word_count(word_to_count):
    width = len(max(word_to_count))
    for word in word_to_count:
        print(f"{word:{width}} is {word_to_count[word]}")


def turn_text_into_dictionary(text, word_to_count):
    for word in text:
        word_to_count[word] = count_word(word, text)


def count_word(word, text):
    count = 0
    for i in text:
        if i == word:
            count += 1
    return count


main()
