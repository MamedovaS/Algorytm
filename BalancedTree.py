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

        stack = [(node, False)]
        depths = {}

        while stack:
            visitting, visited = stack.pop(0)
            if not visitting:
                depths[visitting] = 0
            elif not visited:
                stack.append((visitting, True))
                stack.append((visitting.right, False))
                stack.append((visitting.left, False))
            else:
                left_depth = depths[visitting.left] if visitting.left in depths else 0
                right_depth = depths[visitting.right] if visitting.right in depths else 0

                if abs(left_depth - right_depth) > 1:
                    return -1

                depths[visitting] = max(left_depth, right_depth) + 1

        return depths[node] != -1

    return get_depth(node) != -1

if __name__ == "__main__":
    root = BinaryTree(50)
    root.left = BinaryTree(17)
    root.left.left = BinaryTree(9)
    root.left.left.right = BinaryTree(14)
    root.left.left.right.left = BinaryTree(12)
    root.left.right = BinaryTree(23)
    root.left.right.left = BinaryTree(19)
    root.right = BinaryTree(76)
    root.right.left = BinaryTree(54)
    root.right.left.right = BinaryTree(72)
    root.right.left.right.left = BinaryTree(67)

    root2 = BinaryTree(50)
    root2.right = BinaryTree(72)
    root2.right.right = BinaryTree(76)
    root2.right.left = BinaryTree(54)
    root2.right.left.right = BinaryTree(67)
    root2.left = BinaryTree(17)
    root2.left.right = BinaryTree(23)
    root2.left.right.left = BinaryTree(19)
    root2.left.left = BinaryTree(12)
    root2.left.left.right = BinaryTree(14)
    root2.left.left.left = BinaryTree(9)

    if is_tree_balanced(root):
        print("Дерево збалансоване")
    else:
        print("Дерево не збалансоване")

# O(n), n-num of node


#
# left_depth = get_depth(node.left)
# if left_depth == -1:
#     return -1
# right_depth = get_depth(node.right)
# if right_depth == -1:
#     return -1
#
# if abs(left_depth - right_depth) > 1:
#     return -1
#
# return max(left_depth, right_depth) + 1
