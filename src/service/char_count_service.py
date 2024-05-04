from .file_object_service import get_data_as_file


def count_chars(data, data_type):
    chars = 0
    data = get_data_as_file(data, data_type, encoding='utf-8')
    for line in data:
        chars += len(line)

    return chars
