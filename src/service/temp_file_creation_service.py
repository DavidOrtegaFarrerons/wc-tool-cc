import tempfile


def create_temp_file(data):
    temporary_file = tempfile.NamedTemporaryFile(mode='w+t', delete=False)

    for line in data:
        temporary_file.write(line)

    temporary_file.seek(0)
    temporary_file.close()

    return temporary_file
