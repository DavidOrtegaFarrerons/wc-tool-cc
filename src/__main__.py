from .parser.cli_parser import get_arguments
from .dispatcher.argument_dispatcher import argument_dispatch


def main():
    [cli_option, file_path] = get_arguments()
    argument_dispatch(cli_option, file_path)


main()
