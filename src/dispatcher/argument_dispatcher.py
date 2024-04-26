from ..service.byte_count_service import count_bytes
from ..service.line_count_service import count_lines
from ..service.word_count_service import count_words
from ..service.char_count_service import count_chars


def argument_dispatch(argument, file_path):
    actions = {
        "-c": count_bytes,
        "-l": count_lines,
        "-w": count_words,
        "-m": count_chars,
        "": lambda x: f"{count_lines(x)} {count_words(x)} {count_bytes(x)}"
    }

    # Check if the provided argument has a corresponding function
    if argument in actions:
        result = actions[argument](file_path)
        print(f"{result} {file_path}")
    else:
        raise Exception("Invalid argument")

