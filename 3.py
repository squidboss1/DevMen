
def remove_repetitions(text):
    lines_of_words = text.split()
    words_without_repetitions = []

    for word in lines_of_words:
        if word not in words_without_repetitions:
            words_without_repetitions.append(word)
    new_text = ' '.join(words_without_repetitions)

    # print(new_text)
    return new_text

with open('przyklad2.txt', 'r', encoding="utf-8") as input_file:
    text = input_file.readlines()
    new_text = [remove_repetitions(line) for line in text]

with open('przyklad2_rozwiazanie.txt', 'w', encoding="utf-8") as output_file:
    output_file.write('\n'.join(new_text))
