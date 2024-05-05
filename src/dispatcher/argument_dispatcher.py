from src.service.byte_count_service import count_bytes
from src.service.line_count_service import count_lines
from src.service.word_count_service import count_words
from src.service.char_count_service import count_chars

ARG_COUNT_BYTES = "-c"
ARG_COUNT_LINES = "-l"
ARG_COUNT_WORDS = "-w"
ARG_COUNT_CHARS = "-m"
ARG_COUNT_LINES_WORDS_BYTES = ""


def argument_dispatch(argument, filename):
    actions = {
        ARG_COUNT_BYTES: count_bytes,
        ARG_COUNT_LINES: count_lines,
        ARG_COUNT_WORDS: count_words,
        ARG_COUNT_CHARS: count_chars,
        ARG_COUNT_LINES_WORDS_BYTES: lambda x: f"{count_lines(x)} {count_words(x)} {count_bytes(x)}"
    }

    if argument in actions:
        result = actions[argument](filename)
        is_temporary_file = filename.endswith('.txt')
        print(f"{result} {filename if is_temporary_file else ''}")
    else:
        raise Exception("Invalid argument")
