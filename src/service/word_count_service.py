from .file_object_service import get_data_as_file


def count_words(data, data_type):
    words = 0
    data = get_data_as_file(data, data_type, encoding='utf-8')
    for line in data:
        words += len(line.split())

    return words
