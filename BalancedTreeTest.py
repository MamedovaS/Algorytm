import unittest

from BalancedTree import BinaryTree, is_tree_balanced


class TestIsTreeBalanced(unittest.TestCase):
    def test_balanced_tree(self):
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)
        root.right.left = BinaryTree(15)
        root.right.right = BinaryTree(7)
        self.assertTrue(is_tree_balanced(root))

    def test_unbalanced_tree(self):
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)
        root.right.left = BinaryTree(15)
        root.right.right = BinaryTree(7)
        root.right.left.left = BinaryTree(10)  # Додаємо незбалансований вузол
        self.assertFalse(is_tree_balanced(root))

    def test_empty_tree(self):
        self.assertTrue(is_tree_balanced(None))

    def test_single_node_tree(self):
        root = BinaryTree(5)
        self.assertTrue(is_tree_balanced(root))

if __name__ == '__main__':
    unittest.main()
