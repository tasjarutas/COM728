def display_chars(file_path, num_of_chars):
    with open(file_path) as file:
        data = file.read(num_of_chars)
        print(data)


def display_line(file_path):
    with open(file_path) as file:
        data = file.readline().strip()
        print(data)


def display_text(file_path):
    with open(file_path) as file:
        data = file.read()
        lines = data.split('\n')
        for line in lines:
            print(line)


def run():
    path = "library.txt"
    print("The first 5 characters are: ")
    display_chars(path, 5)
    print("\nThe first line is: ")
    display_line(path)
    print("\nThe full text is: ")
    display_text(path)


if __name__ == '__main__':
    run()
