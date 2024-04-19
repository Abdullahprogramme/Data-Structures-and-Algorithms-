from HelperFunctions import *

def Question2():
    nodes = ["begin", "do", "else", "end", "if", "then", "while"]
    bst = {}
    for i in nodes:
        insert(bst, i)
    print(bst)

## Testing
Question2()

## Expected Output
# {'value': 'begin', 'left': {}, 'right': {'value': 'do', 'left': {}, 'right': {'value': 'else', 'left': {}, 'right': {'value': 'end', 'left': {}, 'right': {'value': 'if', 'left': {}, 'right': {'value': 'then', 'left': {}, 'right': {'value': 'while', 'left': {}, 'right': {}}}}}}}}