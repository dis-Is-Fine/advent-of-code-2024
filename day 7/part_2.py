import os
import time
import datetime
import re

__test = True

__baseDir = os.path.dirname(__file__)

__testSet = [
    [os.path.join(__baseDir, "example_input.txt"), 11387]
]

__inputFile = os.path.join(__baseDir, 'input.txt')

def temp(possibilities, number):
    new_possibilities = []
    for p in possibilities:
        new_possibilities.append(p+number)
        new_possibilities.append(p*number)
        new_possibilities.append(int(str(p)+str(number)))
    return new_possibilities

def solve(input):
    solution = 0

    for line in input:
        numbers = re.findall(r'\d+', line)
        result = int(numbers.pop(0))
        combinations = [int(numbers.pop(0))]
        while len(numbers) > 0:
            combinations = temp(combinations, int(numbers.pop(0)))
        
        for c in combinations:
            if c == result:
                solution += result
                break

    print(solution)
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
    print(f'Tests completed succesfully in: {__runTime}\n{"="*45}')


try:
    input = open(__inputFile, 'r')
except FileNotFoundError as e:
    raise (e)

__startTime = time.time()

solution = solve(input)

__runTime = datetime.datetime.fromtimestamp(time.time()-__startTime).strftime('%S.%fs')
print(f'Solution for the puzzle: {solution}\nElapsed time: {__runTime}')