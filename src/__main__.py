from .parser.cli_parser import get_cli_arguments
from .dispatcher.argument_dispatcher import argument_dispatch


def main():
    cli_selected_option, file_path = get_cli_arguments()
    argument_dispatch(cli_selected_option, file_path)


main()
