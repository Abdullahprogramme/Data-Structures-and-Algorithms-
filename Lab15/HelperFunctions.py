# Helper Function #1
def insert(bst, key):
    if bst == {}:
        bst['value'] = key
        bst['left'] = {}
        bst['right'] = {}
    else:
        if key > bst['value']:
            insert(bst['right'], key)
        else:
            insert(bst['left'], key)
        

# Helper Function #2
def exist(bst, key):
    if bst != {} and bst['value'] == key:
        return True
    elif bst != {} and bst['value'] < key:
        return exist(bst['right'], key)
    elif bst != {} and bst['value'] > key:
        return exist(bst['left'], key)
    return False

# Helper Function #3
def minimum(bst, starting_node):
    if bst != {} and bst['value'] < starting_node:
        return minimum(bst['right'], starting_node)
    elif bst != {} and bst['value'] > starting_node:
        return minimum(bst['left'], starting_node)
    else:
        if bst['left'] != {}:
            return find_min(bst['left'])
        else: return bst

def find_min(bst):
    if bst['left'] != {}:
        return find_min(bst['left'])
    return bst

# Helper Function #4
def maximum(bst,starting_node):
    if bst != {} and bst['value'] < starting_node:
        return maximum(bst['right'], starting_node)
    elif bst != {} and bst['value'] > starting_node:
        return maximum(bst['left'], starting_node)
    else:
        if bst['right'] != {}:
            return find_max(bst['right'])
        else: return bst

def find_max(bst):
    if bst['right'] != {}:
        return find_max(bst['right'])
    return bst

# Helper Function #5
def inorder_traversal(bst, res):
    if bst != {}:
        inorder_traversal(bst['left'], res)
        res.append(bst['value'])
        inorder_traversal(bst['right'], res)
    
# Helper Function #6
def preorder_traversal(bst, res):
    if bst != {}:
        res.append(bst['value'])
        preorder_traversal(bst['left'], res)
        preorder_traversal(bst['right'], res)

# Helper Function #7
def postorder_traversal(bst, res):
    if bst != {}:
        postorder_traversal(bst['left'], res)
        postorder_traversal(bst['right'], res)
        res.append(bst['value'])
    
    
# Helper Function #8
def successor(BST, key, successor_node=None):
    if BST != {} and key < BST['value']:
        return successor(BST['left'], key, BST['value'])
    elif BST != {} and key > BST['value']:
        return successor(BST['right'], key, successor_node)
    else:
        if BST['right'] != {}:
            return successor_min(BST['right'])
        else: return successor_node

def successor_min(bst):
    if bst['left'] != {}:
        return successor_min(bst['left'])
    return bst['value']
