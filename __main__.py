import sys


def how_to_use_command():
    print("To run this command, please use \"python __main__.py -c example_file.txt")


def get_arguments():
    cli_option = sys.argv[1]
    file_path = sys.argv[2]

    if cli_option is None or file_path is None:
        raise Exception(how_to_use_command)

    return cli_option, file_path


def count_file_bytes(file_path):
    file = open(file_path, "rb")  # [r]eading as [b]inary

    with open(file_path, "rb") as file:
        return len(file.read())


def cli_options(cli_option, file_path):
    if cli_option == "-c":
        print(str(count_file_bytes(file_path)) + " " + file_path)


def main():
    [cli_option, file_path] = get_arguments()
    cli_options(cli_option, file_path)


main()
