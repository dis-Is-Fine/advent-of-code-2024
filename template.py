import os

test = False

baseDir = os.path.join(os.path.dirname(os.path.abspath(__file__)),os.path.pardir)

inputFile = os.path.join(baseDir, 'example_input.txt' if test else 'input.txt')
input = open(inputFile, 'r')