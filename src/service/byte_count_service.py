from .file_object_service import get_data_as_file
from ..parser.cli_parser import INPUT_TYPE_FILE


def count_bytes(data, data_type):
    if data_type == INPUT_TYPE_FILE:
        with get_data_as_file(data, True, "rb") as file:
            return len(file.read())
    else:
        return len(data.encode('utf-8'))
