from .file_object_service import get_data_as_file


def count_lines(data, data_type):
    data = get_data_as_file(data, data_type, encoding='utf-8')
    return len(data.readlines())
