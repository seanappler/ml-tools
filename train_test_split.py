from random import random
import argparse


parser = argparse.ArgumentParser(
    description="This script randomly selects a subset of the dataset.")
parser.add_argument("-d", "--dataset", type=str)
parser.add_argument("-r", "--ratio", type=float,
                    help="the ratio of subset to the data set.",
                    default=0.2)
args = parser.parse_args()


with open('out.train', 'w') as file_base, open('out.test', 'w') as file_test:
    for line in open(args.dataset):
        if random() > args.ratio:
            file_base.write(line)
        else:
            file_test.write(line)
