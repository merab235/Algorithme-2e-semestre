import unittest
from lab2.lab_13.src.task13 import AVLTree

class TestAVLTree(unittest.TestCase):
    def test_small_left_rotation(self):
        nodes = [
            (10, 5, 15),
            (5, 0, 0),
            (15, 12, 20),
            (12, 0, 0),
            (20, 0, 0)
        ]
        avl = AVLTree(nodes)
        rotated_tree = avl.left_rotate()
        expected_tree = {
            15: (10, 20),
            10: (5, 12),
            5: (0, 0),
            12: (0, 0),
            20: (0, 0)
        }
        self.assertEqual(rotated_tree, expected_tree)

    def test_no_rotation_needed(self):
        nodes = [
            (10, 5, 0),
            (5, 0, 0)
        ]
        avl = AVLTree(nodes)
        rotated_tree = avl.left_rotate()
        self.assertEqual(rotated_tree, avl.tree)

    def test_large_tree_rotation(self):
        nodes = [
            (30, 20, 40),
            (20, 10, 25),
            (40, 35, 50),
            (10, 0, 0),
            (25, 0, 0),
            (35, 0, 0),
            (50, 0, 0)
        ]
        avl = AVLTree(nodes)
        rotated_tree = avl.left_rotate()
        expected_tree = {
            40: (30, 50),
            30: (20, 35),
            20: (10, 25),
            10: (0, 0),
            25: (0, 0),
            35: (0, 0),
            50: (0, 0)
        }
        self.assertEqual(rotated_tree, expected_tree)

    def test_rotation_on_single_node(self):
        nodes = [
            (10, 0, 0)
        ]
        avl = AVLTree(nodes)
        rotated_tree = avl.left_rotate()
        self.assertEqual(rotated_tree, avl.tree)

if __name__ == "__main__":
    unittest.main()


