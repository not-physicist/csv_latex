# use python 3


import csv
#  import sys
from argparse import ArgumentParser


# Function to see if the input string is/can be converted to number
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def delSwitcher(x):
    switcher = {
        'tab': '\t',
        'space': ' ',
        ',': ',',
        ';': ';',
    }
    return switcher.get(x, "Invalid delimiter!")


parser = ArgumentParser()
parser.add_argument("-i", "--input", dest="input", required=True,
                    help="input file name", metavar="FILE")
parser.add_argument("-d", "--delimiter", dest="delimiter", default=",",
                    help="delimiter used to parse input", metavar="DELIMITer")
parser.add_argument("-s", "--skip_header", dest="header", default=0,
                    help="number of lines in the begining to skip")
parser.add_argument("-o", "--output", dest="output", default=None,
                    help="specify output tex file")
args = parser.parse_args()
#  print(args.input)
#  print(args.delimiter)

args.delimiter = delSwitcher(args.delimiter)
#  print(args.delimiter)

header = int(args.header)
#  print(header)

# TODO: also output tex environment
# TODO: output to file
#  print(r"\begin{tabular}{}")
#  print(r"\toprule")
#  print(r"\midrule")
with open(args.input, newline="") as csvfile:
    a = csv.reader(csvfile, delimiter=args.delimiter)
    # a is a object containing row arrays
    for row in a:
        for i in row:   # i is each element
            if  header > 0:
                header -= 1
                break
            if not is_number(i):    # if not a number, must be header
                print(i, end="")
            else:
                print(r"\num{" + i + "}", end="")
            if i == row[-1]:  # if last entry of the line
                print(r"\\")
            else:
                print(" & ", end="")
#  print(r"\bottomrule")
#  print(r"\end{tabular}")
