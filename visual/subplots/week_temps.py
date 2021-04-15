import matplotlib.pyplot as plt
import csv


def read_data():
    data = {'week1':[],'week2':[]}
    with open("temps.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        header = next(csv_reader)

        for row in csv_reader:
            data['week1'].append(int(row[0].strip()))
            data['week2'].append(int(row[0].strip()))
    return data


def run():
    data = read_data()
    fig, (ax1, ax2) = plt.subplots(1,2)
    ax1.plot(range(len(data['week1'])), data['week1'])
    ax2.plot(range(len(data['week2'])), data['week2'])
    plt.show()





run()
