import os
import csv

def read_csv_data_file(DATASET, INPUT_FOLDER):
# ##########################
# Load Data in '.csv' format: filename, class, 0|1|2 (learning, validation, test)

    learning_samples = []
    validation_samples = []
    test_samples = []
    classes = []
    with open(DATASET) as f:
        csv_file = csv.reader(f, delimiter=',')
        for row in csv_file:
            # print(row[11])
            if int(row[-1]) == 0:
                learning_samples.append(row[0:-1])
            if int(row[-1]) == 1:
                validation_samples.append(row[0:-1])
            if int(row[-1]) == 2:
                test_samples.append(row[0:-1])
            classes.append(row[-2])

    for row in learning_samples:
        row[-1] = int(row[-1])
    for row in validation_samples:
        row[-1] = int(row[-1])
    for row in test_samples:
        row[-1] = int(row[-1])

    classes = list(set(classes))

    return learning_samples, validation_samples, test_samples, classes


