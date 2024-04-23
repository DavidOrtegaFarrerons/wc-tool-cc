def count_bytes(file_path):
    with open(file_path, "rb") as file:  # [r]eading as [b]inary
        return len(file.read())
