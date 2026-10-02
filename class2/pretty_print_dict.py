def pretty_print_dict(d, indent=0, indent_step=4):
    """
    Печатает словарь произвольной вложенности в читаемом виде.
    :param d: словарь
    :param indent: текущий уровень отступа (в пробелах)
    :param indent_step: сколько пробелов добавлять на каждый уровень
    """
    pad = " " * indent
    inner_pad = " " * (indent + indent_step)

    print("{")

    items = list(d.items())
    for i, (key, value) in enumerate(items):
        comma = "," if i < len(items) - 1 else ""

        if isinstance(value, dict):
            print(f'{inner_pad}"{key}": ', end="")
            pretty_print_dict(value, indent + indent_step, indent_step)
            print(comma)
        else:
            print(f'{inner_pad}"{key}": {repr_value(value)}{comma}')

    print(f"{pad}}}", end="")


def repr_value(value):
    """Возвращает значение в виде, похожем на JSON"""
    if isinstance(value, str):
        return f'"{value}"'
    if value is True:
        return "true"
    if value is False:
        return "false"
    if value is None:
        return "null"
    return str(value)


if __name__ == "__main__":
    print("Пример 1")
    pretty_print_dict({
        "name": "John",
        "age": 30,
        "address": {"city": "NY", "zip": 10001}
    })

    print("\nПример 2")
    pretty_print_dict({
        "a": 1,
        "b": {"c": {"d": [1, 2, 3], "e": None}, "f": True},
        "g": "hello"
    })