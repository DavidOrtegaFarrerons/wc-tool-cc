from ..service.byte_count_service import count_bytes
from ..service.line_count_service import count_lines


def argument_dispatch(argument, file_path):
    if argument == "-c":
        print(str(count_bytes(file_path)) + " " + file_path)

    if argument == "-l":
        print(str(count_lines(file_path)) + " " + file_path)
