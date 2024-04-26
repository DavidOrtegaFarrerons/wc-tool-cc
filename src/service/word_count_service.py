def count_words(file_path):
    word_counter = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            word_counter += len(line.split())

    return word_counter
