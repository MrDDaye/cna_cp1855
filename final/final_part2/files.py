"""Functions for baseball team manager file handling."""
from csv import reader, writer

def save_to_file(file: str, rows: list[list[str]]) -> None:
    """Save row data to the selected file."""
    with open(file, 'w', newline='',encoding='utf-8') as save_file:
        csv = writer(save_file)
        csv.writerows(rows)

def read_from_file(file: str) -> list[list[str]]:
    """Read row data from the selected file."""
    with open(file, 'r', encoding='utf-8') as read_file:
        csv = reader(read_file)
        return [row for row in csv]