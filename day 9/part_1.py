import os
import time
import datetime

__test = True

__baseDir = os.path.dirname(__file__)

__testSet = [
    [os.path.join(__baseDir, "example_input.txt"), 1928]
]

__inputFile = os.path.join(__baseDir, 'input.txt')


def solve(input):
    solution = 0

    disk = []
    empty = []
    x = 0

    for line in input:
        for i, char in enumerate(line.strip()):
            if i%2 == 0:
                for a in range(int(char)):
                    disk.append(x)
                x += 1
            else:
                for a in range(int(char)):
                    disk.append('.')

    for i, c in enumerate(disk):
        if c == '.':
            empty.append(int(i))

    for i in reversed(range(len(disk))):
        if len(empty) == 0:
            break
        if disk[i] != '.':
            if empty[0] >= i:
                break
            disk[empty.pop(0)] = disk[i]
            disk[i] = '.'

    for i, part in enumerate(disk):
        if part == '.':
            break
        solution += i*int(part)

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