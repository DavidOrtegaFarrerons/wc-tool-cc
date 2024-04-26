from ..service.byte_count_service import count_bytes
from ..service.line_count_service import count_lines
from ..service.word_count_service import count_words
from ..service.char_count_service import count_chars


def argument_dispatch(argument, file_path):
    if argument == "-c":
        print(str(count_bytes(file_path)) + " " + file_path)

    if argument == "-l":
        print(str(count_lines(file_path)) + " " + file_path)

    if argument == "-w":
        print(str(count_words(file_path)) + " " + file_path)

    if argument == "-m":
        print(str(count_chars(file_path)) + " " + file_path)
