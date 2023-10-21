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
        root.left = BinaryTree(90)
        root.right = BinaryTree(20)
        root.right.left = BinaryTree(105)
        root.right.right = BinaryTree(70)
        root.right.left.left = BinaryTree(100)
        self.assertFalse(is_tree_balanced(root))

    def test_empty_tree(self):
        self.assertTrue(is_tree_balanced(None))

    def test_single_node_tree(self):
        root = BinaryTree(5)
        self.assertTrue(is_tree_balanced(root))

if __name__ == '__main__':
    unittest.main()
