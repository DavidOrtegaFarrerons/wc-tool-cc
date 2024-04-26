import os
import sys

from ..error.no_arguments import no_arguments


def get_cli_arguments():
    if len(sys.argv) < 3:
        if os.path.isfile(sys.argv[1]):
            return '', sys.argv[1]
        else:
            raise Exception(no_arguments())

    cli_option = sys.argv[1]
    file_path = sys.argv[2]

    return cli_option, file_path
