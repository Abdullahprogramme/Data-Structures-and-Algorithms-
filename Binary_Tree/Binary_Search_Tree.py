def create():
    return {'left': {}, 'right': {}, 'value': {}}

def search(tree, val):
    if tree['value'] == None or tree['value'] == val:
        return True
    if tree['value'] != {} and tree['value'] > val:
        return search(tree['left'], val)
    elif tree['value'] != {} and tree['value'] < val:
        return search(tree['right'], val)
    return False
    
def find_min(tree):
    while tree['left'] and tree['left']['value'] != {}:
        tree = tree['left']
    return tree['value']

def find_max(tree):
    while tree['right'] and tree['right']['value'] != {}:
        tree = tree['right']
    return tree['value']

def insert(tree, val):
    if tree['value'] == {}:
        tree['value'] = val
        tree['left'] = create()
        tree['right'] = create()
    elif tree['value'] > val:
        insert(tree['left'], val)
    else:
        insert(tree['right'], val)

def successor(tree, val):
    parent = None
    while val != tree['value']:
        if val < tree['value']:
            parent = tree['value']
            tree = tree['left']
        else:
            tree = tree['right']
    if tree['right'] == {}:
        return parent
    else: 
        return find_min(tree['right'])
    
def delete(tree, val, parent=None):
    if tree['value'] == {}:
        return False
    if val < tree['value']:
        delete(tree['left'], val, tree)
    elif val > tree['value']:
        delete(tree['right'], val, tree)
    else:
        if tree['left'] == {} and tree['right'] == {}:
            if parent['left'] == tree:
                parent['left'] = {}
            else:
                parent['right'] = {}
        elif tree['right'] == {}:
            if parent['left'] == tree:
                parent['left'] = tree['left']
            else:
                parent['right'] = tree['left']
        elif tree['left'] == {}:
            if parent['left'] == tree:
                parent['left'] = tree['right']
            else:
                parent['right'] = tree['right']
        else:
            min_val = find_min(tree['right'])
            tree['value'] = min_val
            delete(tree['right'], min_val, tree)
    return True

def inorder(tree):
    if tree['value'] == {}:
        return []
    return inorder(tree['left']) + [tree['value']] + inorder(tree['right'])

def preorder(tree):
    if tree['value'] == {}:
        return []
    return [tree['value']] + preorder(tree['left']) + preorder(tree['right'])

def postorder(tree):
    if tree['value'] == {}:
        return []
    return postorder(tree['left']) + postorder(tree['right']) + [tree['value']]