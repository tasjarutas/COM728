import matplotlib.pyplot as plt
import csv


def read_data():
    data={'survived':[], 'sex':[], 'age':[], 'fare':[]}
    with open("titanic.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        #extract headers
        headers = next(csv_reader)
        for line in csv_reader:
            survived = line[1].strip()
            sex = line[14].strip()
            age = line[4].strip()
            fare = line[8].strip()
            # only add the data to the dictionary if not empty
            if survived != "" and sex != "" and age != "" and fare != "":
                data['survived'].append(bool(int(survived)))

                if int(sex) == 0:
                    data['sex'].append('male')
                else:
                    data['sex'].append('female')

                data['age'].append(float(age))
                data['fare'].append(round(float(fare), 2))
    return data

def plot_fare_vs_survival(ax,data):
    survived = []
    deceased = []

    for index in range(len(data['fare'])):
        fare = data['fare'][index]
        if data['survived'][index]:
            survived.append(data['fare'][index])
        else:
            deceased.append(data['fare'][index])

    ax.scatter(range(len(survived)), survived, label='Survived')
    ax.scatter(range(len(deceased)), deceased, label='Deceased')
    ax.set_ylabel('fare')
    ax.legend()
    ax.set_title('Fare vs Survival')

def run():
    data = read_data()
    #print(data)
    # plots arranged in a 2 by 2 grid
    fig, axs = plt.subplots(2, 2)
    # display plots
    plot_fare_vs_survival(axs[0, 1], data)
    plt.tight_layout()
    plt.show()


run()
