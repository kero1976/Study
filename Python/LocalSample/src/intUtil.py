import math


def convert_size(size: int) -> str:
    units = ("B", "KB", "MB", "GB", "TB")
    i = math.floor(math.log(size, 1024)) if size > 0 else 0
    size = round(size / 1024 ** i, 2)

    return f"{size} {units[i]}"


print(convert_size(1000 * 1000 * 38))