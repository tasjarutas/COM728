import csv


def extract(file_name):
    names=[]
    print ("Extracting...")
    with open(file_name) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)

        for values in csv_reader:
            names.append(values[1]+"\n")
        print("Done! The extracted names are as follows:")
        for name in names:
            print(name)


def run():
    extract("bots.csv")


if __name__ == "__main__":
    run()
