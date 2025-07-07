from pathlib import Path

def get_size(path: Path) -> int:
    if path.is_file():
        return path.stat().st_size
    elif path.is_dir():
        return sum(get_size(child) for child in path.iterdir())
    return 0

def traverse_directory(directory: Path, prefix=""):
    items = list(directory.iterdir())
    last_index = len(items) - 1

    for idx, item in enumerate(items):
        size_kb = get_size(item) / 1024
        connector = "└── " if idx == last_index else "├── "
        if item.is_file():
            print(f"{prefix}{connector}{item.name} ({size_kb:.2f} KB)")
        elif item.is_dir():
            print(f"{prefix}{connector}{item.name} ({size_kb:.2f} KB)")
            extentsion = '    ' if idx == last_index else '│   '
            traverse_directory(item, prefix + extentsion)


curr_dir = Path(__file__).parent.absolute()
print()
print(f"{curr_dir.name} ({get_size(curr_dir) / 1024:.2f} KB)")
traverse_directory(curr_dir)
