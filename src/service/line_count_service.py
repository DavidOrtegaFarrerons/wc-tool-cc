def count_lines(file_path):
    # [r]eading as text (default). Encode added to prevent OS issues
    with open(file_path, "r", encoding='utf-8') as file:
        return len(file.readlines())
