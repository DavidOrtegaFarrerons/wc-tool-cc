import os
import sys

from ..error.no_arguments import no_arguments


def get_cli_selected_option():
    return sys.argv[2] if len(sys.argv) == 3 else ""


INPUT_TYPE_FILE = 'file'
INPUT_TYPE_STDIN = 'stdin'


def get_cli_input():
    input_arg = sys.argv[1]
    if input_arg != "":
        if os.path.isfile(input_arg):
            return INPUT_TYPE_FILE, input_arg
        return INPUT_TYPE_STDIN, input_arg
    else:
        raise Exception(no_arguments())
