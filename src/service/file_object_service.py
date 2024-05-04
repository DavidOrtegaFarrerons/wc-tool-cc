import io
from src.parser.cli_parser import INPUT_TYPE_FILE


def get_data_as_file(data, data_type=INPUT_TYPE_FILE, mode="r", encoding=None):
    if data_type == INPUT_TYPE_FILE:
        return open(data, mode, encoding=encoding)
    else:
        return io.StringIO(data)
