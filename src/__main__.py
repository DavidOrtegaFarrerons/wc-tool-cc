from src.parser.cli_parser import get_cli_input, get_cli_selected_option
from src.dispatcher.argument_dispatcher import argument_dispatch


def main():
    cli_selected_option = get_cli_selected_option()
    filename = get_cli_input()
    argument_dispatch(cli_selected_option, filename)


main()
