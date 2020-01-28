def traverse_tree(node):
    if not node.children:
        yield node
    for child in node.children: 
        yield from traverse_tree(child)