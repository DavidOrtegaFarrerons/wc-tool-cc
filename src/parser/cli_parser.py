import sys

from ..error.no_arguments import no_arguments


def get_arguments():
    if len(sys.argv) < 3:
        raise Exception(no_arguments())
    cli_option = sys.argv[1]
    file_path = sys.argv[2]

    return cli_option, file_path
