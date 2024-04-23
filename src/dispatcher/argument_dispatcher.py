from ..service.byte_count_service import count_bytes


def argument_dispatch(argument, file_path):
    if argument == "-c":
        print(str(count_bytes(file_path)) + " " + file_path)
