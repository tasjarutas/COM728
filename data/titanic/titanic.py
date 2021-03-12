import csv
records = []
headings = []


def load_data(file_path):
    print("Loading data...")
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        headings_list = next(csv_reader)
        for heading in headings_list:
            headings.append(heading)
        print(headings)

        for index in range(len(csv_reader)):
            records.append(csv_reader[index])
        print(records)



def run():
    load_data('titanic.csv')


if __name__ == '__main__':
    run()
