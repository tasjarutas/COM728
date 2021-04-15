import matplotlib.pyplot as plt


def read_data(file_name):
    temps = []
    with open(file_name) as file:
        for temp in file:
            temps.append(int(temp.strip()))
    return temps


def run():
    data = read_data('temps.txt')
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(range(len(data)), data)
    ax2.bar(range(len(data)), data)
    plt.show()


if __name__ == '__main__':
    run()
