import os
import time
import datetime
import re

__test = True

__baseDir = os.path.dirname(__file__)

__testSet = [
    [os.path.join(__baseDir, 'example_input_part_2.txt'), 48]
]

__inputFile = os.path.join(__baseDir, 'input.txt')

def solve(input):
    regexFunction = r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)'
    regexArgument = r'\d{1,3}'

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
    
    return solution

def test(testSet):
    for i, [testInputFile, solution] in enumerate(testSet, 1):
        try:
            testInput = open(testInputFile, 'r')
        except FileNotFoundError as e:
            raise(e)
        
        if solve(testInput) != solution:
            raise RuntimeError(f'Test {i} failed!')

        else:
            yield f'Test {i} passed'

if __test:
    __startTime = time.time()

    for msg in test(__testSet):
        print(msg)

    __runTime = datetime.datetime.fromtimestamp(time.time()-__startTime).strftime('%S.%fs')
    print(f'Tests completed succesfully in: {__runTime}\n{'='*45}')


try:
    input = open(__inputFile, 'r')
except FileNotFoundError as e:
    raise (e)

__startTime = time.time()

solution = solve(input)

__runTime = datetime.datetime.fromtimestamp(time.time()-__startTime).strftime('%S.%fs')
print(f'Solution for the puzzle: {solution}\nElapsed time: {__runTime}')
