def say_hello(name):
    return f"Hello, {name}!"


def main():
    name = input("Enter your name: ")

    message = say_hello(name)

    print(message)


if __name__ == "__main__":
    main()