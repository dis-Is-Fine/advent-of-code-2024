import os
import time
import datetime
import re

__test = True

__baseDir = os.path.dirname(__file__)

__testSet = [
    [os.path.join(__baseDir, "example_input.txt"), 143]
]

__inputFile = os.path.join(__baseDir, 'input.txt')

def solve(input):
    solution = 0

    rules = []
    updates = []

    for line in input:
        if line == '\n':
            continue
        if line.find('|') < 0:
            updates.append(list(map(int, re.findall(r'\d+', line))))
        else:    
            rules.append(list(map(int, re.findall(r'\d+', line))))

    for i, update in enumerate(updates, 1):
        updateCorrect = True

        for rule in rules:
            ruleLeft: int
            ruleRight: int

            try:
                ruleLeft = update.index(rule[0])
            except ValueError as e:
                continue

            try:
                ruleRight = update.index(rule[1])
            except ValueError as e:
                continue

            if ruleLeft > ruleRight:
                updateCorrect = False
                break
        
        if not updateCorrect:
            continue

        solution += update[int(len(update)/2)]

    return solution


def test(testSet):
    for i, [testInputFile, solution] in enumerate(testSet, 1):
        try:
            testInput = open(testInputFile, 'r')
        except FileNotFoundError as e:
            raise(e)
        
        result = solve(testInput)

        if result != solution:
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