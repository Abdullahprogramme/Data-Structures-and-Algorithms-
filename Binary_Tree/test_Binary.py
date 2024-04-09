import pytest
from Binary_Search_Tree import create, insert, search, find_min, find_max, inorder, preorder, postorder, delete, successor

@pytest.fixture
def setup_tree():
    tree = create()
    insert(tree, 20)
    insert(tree, 5)
    insert(tree, 2)
    insert(tree, 9)
    insert(tree, 12)
    insert(tree, 15)
    insert(tree, 19)
    insert(tree, 13)
    insert(tree, 17)
    return tree

def test_search(setup_tree):
    assert search(setup_tree, 12) == True
    assert search(setup_tree, 10) == False
    assert search(setup_tree, 19) == True
    assert search(setup_tree, 20) == True
    assert search(setup_tree, 1) == False

def test_find_min_max(setup_tree):
    assert find_min(setup_tree) == 2
    assert find_max(setup_tree) == 20

def test_traversal(setup_tree):
    assert inorder(setup_tree) == [2, 5, 9, 12, 13, 15, 17, 19, 20]
    assert preorder(setup_tree) == [20, 5, 2, 9, 12, 15, 13, 19, 17]
    assert postorder(setup_tree) == [2, 13, 17, 19, 15, 12, 9, 5, 20]

def test_delete(setup_tree):
    delete(setup_tree, 17)
    delete(setup_tree, 15)
    delete(setup_tree, 5)
    assert inorder(setup_tree) == [2, 9, 12, 13, 19, 20]
    assert successor(setup_tree, 12) == 13
    assert successor(setup_tree, 13) == 19