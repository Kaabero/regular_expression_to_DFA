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

        assert self.tree.root.character == '.'
        assert self.tree.root.right.character == '#'
        assert self.tree.root.left.character == 'a'
        assert self.tree.root.right.parent == self.tree.root
        assert self.tree.root.left.parent == self.tree.root
        assert self.tree.focus_node == self.tree.root

    def test_add_creates_both_right_and_left_child_for_union_operator(self):
        postfix = get_postfix('(a|b).#')
        self.assertEqual(postfix, ['a', 'b', '|', '#', '.'])
        self.tree.build_tree(postfix)

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

        assert self.tree.root.left.character == 'a'
        assert self.tree.root.right.character == '.'
        assert self.tree.root.right.left.character == '*'
        assert self.tree.root.right.left.right is None
        assert self.tree.root.right.left.left.character == 'b'
        assert self.tree.root.left.parent == self.tree.root
        assert self.tree.focus_node == self.tree.root

    def test_add_sets_the_focus_node_correctly(self):
        self.tree.root = Node(1, '.')
        self.tree.root.max_children = 2
        self.tree.focus_node = self.tree.root
        self.tree.add(2, 'a')
        self.tree.add(3, '.')

        assert repr(self.tree.root) == '1'
        assert self.tree.root.character == '.'
        assert self.tree.root.left.character == '.'
        assert self.tree.root.right.character == 'a'
        assert self.tree.focus_node == self.tree.root.left

    def test_get_postfix_works_correctly_when_stack_is_empty(self):
        postfix = get_postfix('a)')
        self.assertEqual(postfix, ['a'])

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

    def test_nullable_firstpos_and_lastpos_are_set_correctly(self):
        postfix = get_postfix('a*.(€|b).#')
        self.assertEqual(postfix, ['a', '*', '€', 'b', '|', '.', '#', '.'])
        self.tree.build_tree(postfix)
        root = self.tree.root
        hash = self.tree.root.right
        cat = self.tree.root.left
        star = self.tree.root.left.left
        union = self.tree.root.left.right
        a = self.tree.root.left.left.left
        epsilon = self.tree.root.left.right.left
        b = self.tree.root.left.right.right
        assert root.character == '.'
        assert cat.character == '.'
        assert hash.character == '#'
        assert star.character == '*'
        assert union.character == '|'
        assert a.character == 'a'
        assert self.tree.root.left.left.right == None
        assert epsilon.character == '€'
        assert b.character == 'b'
        assert self.tree.root.left.right.right.left == None
        assert self.tree.root.left.right.right.right == None
        assert self.tree.root.left.right.left.left == None
        assert self.tree.root.left.right.left.right == None
        assert self.tree.focus_node == self.tree.root

        assert epsilon.nullable == True
        assert star.nullable == True
        assert a.nullable == False
        assert b.nullable == False
        assert union.nullable == True
        assert hash.nullable == False
        assert root.nullable == False
        assert cat.nullable == True

        assert [n.number for n in a.firstpos] == [a.number]
        assert [n.number for n in b.firstpos] == [b.number]
        assert [n.number for n in epsilon.firstpos] == []
        assert [n.number for n in hash.firstpos] == [hash.number]
        assert [n.number for n in star.firstpos] == [a.number]
        assert [n.number for n in union.firstpos] == [b.number]
        assert [n.number for n in cat.firstpos] == [a.number, b.number]
        assert [n.number for n in root.firstpos] == [
            a.number, b.number, hash.number]

        assert [n.number for n in a.lastpos] == [a.number]
        assert [n.number for n in b.lastpos] == [b.number]
        assert [n.number for n in epsilon.lastpos] == []
        assert [n.number for n in hash.lastpos] == [hash.number]

        assert [n.number for n in star.lastpos] == [a.number]
        assert [n.number for n in union.lastpos] == [b.number]
        assert [n.number for n in cat.lastpos] == [a.number, b.number]
        assert [n.number for n in root.lastpos] == [hash.number]

        assert [n.number for n in a.followpos] == [
            a.number, b.number, hash.number]
        assert [n.number for n in b.followpos] == [hash.number]
        assert [n.number for n in epsilon.followpos] == []
        assert [n.number for n in hash.followpos] == []

        assert star.followpos == None
        assert union.followpos == None
        assert cat.followpos == None
        assert root.followpos == None
