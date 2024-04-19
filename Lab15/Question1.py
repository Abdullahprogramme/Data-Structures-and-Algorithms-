from HelperFunctions import *

def Question1():
  pass
  # Question 1a
  bst = {}
  insert(bst, 68)
  insert(bst, 88)
  insert(bst, 61)
  insert(bst, 89)
  insert(bst, 94)
  insert(bst, 50)
  insert(bst, 4)
  insert(bst, 76)
  insert(bst, 66)
  insert(bst, 82)
  print(bst)
  # Question 1b
  print(exist(bst, 50))
  # Question 1c
  print(exist(bst, 49))
  # Question 1d
  print(minimum(bst, 68))
  # Question 1e
  print(minimum(bst, 88))
  # Question 1f
  print(maximum(bst, 68))
  # Question 1g
  print(maximum(bst, 61))
  # Question 1h
  x = []
  inorder_traversal(bst, x)
  print(x)
  # Question 1i
  x = []
  preorder_traversal(bst, x)
  print(x)
  # Question 1j
  x = []
  (postorder_traversal(bst, x))
  print(x)
  # Question 1k
  print(successor(bst, 76))

## Testing
# Question1()

## Expected Outputs
## 1a
# {'value': 68, 'left': {'value': 61, 'left': {'value': 50, 'left': {'value': 4, 'left': {}, 'right': {}}, 'right': {}}, 'right': {'value': 66, 'left': {}, 'right': {}}}, 'right': {'value': 88, 'left': {'value': 76, 'left': {}, 'right': {'value': 82, 'left': {}, 'right': {}}}, 'right': {'value': 89, 'left': {}, 'right': {'value': 94, 'left': {}, 'right': {}}}}}

## 1b
# True 

## 1c
# False 

## 1d
# {'value': 4, 'left': {}, 'right': {}}

## 1e
# {'value': 76, 'left': {}, 'right': {'value': 82, 'left': {}, 'right': {}}}

## 1f
# {'value': 94, 'left': {}, 'right': {}}

## 1g
# {'value': 66, 'left': {}, 'right': {}}

## 1h
# [4, 50, 61, 66, 68, 76, 82, 88, 89, 94]

## 1i
# [68, 61, 50, 4, 66, 88, 76, 82, 89, 94]

## 1j
# [4, 50, 66, 61, 82, 76, 94, 89, 88, 68]

## 1k
# 82