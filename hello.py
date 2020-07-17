def hello_you(name):
    return f"Your Silly: {name}"


def add(x, y):
    result = x + y
    print(f"The result: {result}")


if __name__ == "__main__":
    print(hello_you("Jim"))
    add(3, 4)
