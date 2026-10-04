"""Простой калькулятор — учебный скрипт для практики с git."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


# TODO: добавить функцию divide(a, b)


def main():
    print("2 + 3 =", add(2, 3))
    print("5 - 3 =", subtract(5, 3))  # ожидается 2
    print("4 * 3 =", multiply(4, 3))
    # print("10 / 2 =", divide(10, 2))  # раскомментировать после реализации
    # print("10 / 0 =", divide(10, 0))  # должно вернуть None, а не упасть


if __name__ == "__main__":
    main()
