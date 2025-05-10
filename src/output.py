from rich.table import Table
from rich.console import Console
import os
import json

def print_json(data: dict):
    console = Console()
    console.print_json(data=data)

def print_table(data: list[dict]):
    table = Table()
    for key in data[0].keys():
        table.add_column(key)

    for item in data:
        # Convert all values to strings before adding to table
        row_values = [str(value) for value in item.values()]
        table.add_row(*row_values)

    console = Console()
    console.print(table)
    
def output_to_file(data: dict, filename: str):
    if os.path.exists(filename):
        i = 1
        while os.path.exists(f"{filename}_{i}"):
            i += 1
        filename = f"{filename}_{i}"
    
    with open(filename, "w") as f:
        f.write(json.dumps(data, indent=4))