class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_tree_balanced(node: BinaryTree) -> bool:
    if not node:
        return True

    def get_depth(node):
        if not node:
            return 0
        left_depth = get_depth(node.left)
        if left_depth == -1:
            return -1
        right_depth = get_depth(node.right)
        if right_depth == -1:
            return -1

        if abs(left_depth - right_depth) > 1:
            return -1

        return max(left_depth, right_depth) + 1

    depth = get_depth(node)

    return depth != -1


if __name__ == "__main__":
    root = BinaryTree(3)
    root.left = BinaryTree(9)
    root.right = BinaryTree(20)
    root.right.left = BinaryTree(15)
    root.right.right = BinaryTree(7)

    if is_tree_balanced(root):
        print("Дерево збалансоване")
    else:
        print("Дерево не збалансоване")

#O(n), n-num of node
