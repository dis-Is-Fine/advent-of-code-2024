import os
import time
import datetime
import re

__test = False

baseDir = os.path.join(os.path.dirname(os.path.abspath(__file__)),os.path.pardir)

inputFile = os.path.join(baseDir, 'example_input.txt' if __test else 'input.txt')
input = open(inputFile, 'r')

__startTime = time.time()

regexFunction = 'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)'
regexArgument = '\d{1,3}'

solution = 0
enabled = True

for line in input:
    functions = re.findall(regexFunction, line)
    for function in functions:
        if function == 'do()':
            enabled = True
            continue
        elif function == 'don\'t()':
            enabled = False
            continue
        if not enabled:
            continue

        arguments = re.findall(regexArgument, function)
        solution += int(arguments[0]) * int(arguments[1])

__runTime = datetime.datetime.fromtimestamp(time.time()-__startTime).strftime('%S.%fs')
print(f'Solution for the puzzle: {solution}\nElapsed time: {__runTime}')
