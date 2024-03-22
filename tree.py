class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursion(self.root, value)

    def _insert_recursion(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursion(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursion(node.right, value)
        else:
            pass

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node , value):
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._insert_recursive(node.left, value)
        else:
            return self._insert_recursive(node.right, value)


treenode = BinaryTree()
treenode.insert(1)
treenode.insert(2)
treenode.insert(3)
treenode.insert(4)
treenode.insert(5)

print(treenode.search(1))