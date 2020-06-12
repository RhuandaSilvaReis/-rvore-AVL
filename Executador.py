import random
from ADB import BinarySearchTree

values = random.sample(range(1,100),20)

bst = BinarySearchTree()
for v in values:
    bst.insert(v)

bst.inorder_traversal()

items = [5]
for item in items:
    r = bst.search(item)
    if r is None:
        print(item, 'Não encontrado')
    else:
        print(r.root.data, 'Encontrado')

