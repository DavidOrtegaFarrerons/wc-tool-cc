import os
import sys

from src.error.no_arguments import no_arguments
from src.service.temp_file_creation_service import create_temp_file


def get_cli_selected_option():
    return sys.argv[2] if len(sys.argv) == 3 else ""


INPUT_TYPE_FILE = 'file'
INPUT_TYPE_STDIN = 'stdin'


def get_cli_input():
    if len(sys.argv) < 2 and sys.stdin is not None:
        return create_temp_file(sys.stdin).name

    input_arg = sys.argv[1]

    if input_arg != "" and os.path.isfile(input_arg):
        return input_arg
    else:
        raise Exception(no_arguments())
