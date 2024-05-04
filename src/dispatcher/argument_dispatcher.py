from ..service.byte_count_service import count_bytes
from ..service.line_count_service import count_lines
from ..service.word_count_service import count_words
from ..service.char_count_service import count_chars

ARG_COUNT_BYTES = "-c"
ARG_COUNT_LINES = "-l"
ARG_COUNT_WORDS = "-w"
ARG_COUNT_CHARS = "-m"
ARG_COUNT_LINES_WORDS_BYTES = ""


def argument_dispatch(argument, input_type, input_value):
    actions = {
        ARG_COUNT_BYTES: count_bytes,
        ARG_COUNT_LINES: count_lines,
        ARG_COUNT_WORDS: count_words,
        ARG_COUNT_CHARS: count_chars,
        ARG_COUNT_LINES_WORDS_BYTES: lambda x, y: f"{count_lines(x, y)} {count_words(x, y)} {count_bytes(x, y)}"
    }

    if argument in actions:
        result = actions[argument](input_value, input_type)
        print(f"{result} {input_type}")
    else:
        raise Exception("Invalid argument")
