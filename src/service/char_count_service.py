def count_chars(file_path):
    char_counter = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            char_counter += len(line)

    return char_counter
