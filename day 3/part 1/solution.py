import os
import re

test = False

baseDir = os.path.join(os.path.dirname(os.path.abspath(__file__)),os.path.pardir)

inputFile = os.path.join(baseDir, "example_input.txt" if test else "input.txt")
input = open(inputFile, "r")

regexFunction = "mul\(\d{1,3},\d{1,3}\)"
regexArgument = "\d{1,3}"

solution = 0

for line in input:
    functions = re.findall(regexFunction, line)
    for function in functions:
        arguments = re.findall(regexArgument, function)
        if len(arguments) == 0:
            print("No arguments for function")
            continue
        solution += int(arguments[0]) * int(arguments[1])

print(f'Solution for the puzzle: {solution}')