import unittest
from syntax_tree import SyntaxTree
from utils import get_postfix, get_child_number
from node import Node


class TestSyntaxTree(unittest.TestCase):
    def setUp(self):
        self.tree = SyntaxTree()

    def test_add_creates_both_right_and_left_child_for_concatenation_operator(self):
        postfix = get_postfix('a.#')
        self.assertEqual(postfix, ['a', '#', '.'])
        self.tree.build_tree(postfix)
         
        assert self.tree.root.right is not None
        assert self.tree.root.left is not None
        assert self.tree.root.right.character == '#'
        assert self.tree.root.left.character == 'a'
        assert self.tree.root.right.parent == self.tree.root
        assert self.tree.root.left.parent == self.tree.root
        assert self.tree.focus_node == self.tree.root



    def test_add_both_right_and_left_child_for_union_operator(self):
        postfix = get_postfix('(a|b).#')
        self.assertEqual(postfix, ['a', 'b', '|', '#', '.'])
        self.tree.build_tree(postfix)

        assert self.tree.root.right is not None
        assert self.tree.root.left is not None
        assert self.tree.root.right.character == '#'
        assert self.tree.root.left.character == '|'
        assert self.tree.root.left.right.character == 'b'
        assert self.tree.root.left.left.character == 'a'
        assert self.tree.root.right.parent == self.tree.root
        assert self.tree.root.left.parent == self.tree.root
        assert self.tree.focus_node == self.tree.root
    
    def test_add_creates_only_left_child_for_star_operator(self):
        postfix = get_postfix('a.(b)*.#')
        self.assertEqual(postfix, ['a', 'b', '*', '#', '.', '.'])
        self.tree.build_tree(postfix)


        assert self.tree.root.left is not None
        assert self.tree.root.right is not None
        assert self.tree.root.left.character == 'a'
        assert self.tree.root.right.character == '.'
        assert self.tree.root.right.left.character == '*'
        assert self.tree.root.right.left.right is None
        assert self.tree.root.right.left.left.character == 'b'
        assert self.tree.root.left.parent == self.tree.root
        assert self.tree.focus_node == self.tree.root

    def test_get_tree_returns_dict(self):
        postfix = get_postfix('a.#')
        self.assertEqual(postfix, ['a', '#', '.'])
        self.tree.build_tree(postfix)

        tree = self.tree.get_tree()
        assert isinstance(tree, dict)
        assert 1 in tree
        assert 2 in tree
        assert tree[1]['character'] == '.'
        assert tree[2]['character'] == '#'
        assert tree[3]['character'] == 'a'

        
   