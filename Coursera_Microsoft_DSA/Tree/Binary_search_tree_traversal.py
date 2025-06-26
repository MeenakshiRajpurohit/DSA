class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)

        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)

    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.value, end=' ')
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.value, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=' ')

bst = BinarySearchTree()
values = [50, 30, 70, 20, 40, 60, 80]
for v in values:
    bst.insert(v)
print("Inorder traversal (sorted)")
bst.inorder(bst.root)

print("\n Preorder traversal:")
bst.preorder(bst.root)

print("\n Postorder traversal:")
bst.postorder(bst.root)

     ##      ##BinarySearchTree
           #┌──────────────┐
##root ─────▶│     50       │
           #└────┬────┬────┘
                #│    │
        #┌───────┘    └────────┐
       #30                    70
     # /  \                  /  \
    #20   40              60    80
##