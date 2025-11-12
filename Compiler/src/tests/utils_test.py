import unittest
from utils import validate_input, format_input_for_syntax_tree

class TestValidateInput(unittest.TestCase):
    def test_accepts_valid_input(self):
        assert validate_input("(a|b)*abb")
        assert validate_input("(a|b)*|(a|b)*")
        assert validate_input("(a*|b)*abb")
        assert validate_input("a")
        assert validate_input("ab")
        assert validate_input("(a)")
        assert validate_input("(a|b)")

    def test_rejects_input_with_invalid_symbol(self):
        self.assertRaises(ValueError, validate_input, "(a|b)*#bb")
    def test_rejects_empty_input(self):
        self.assertRaises(ValueError, validate_input, "")
    def test_rejects_input_with_whitespace(self):
        self.assertRaises(ValueError, validate_input, "a b")
    def test_rejects_input_with_unbalanced_parenthesis(self):
        self.assertRaises(ValueError, validate_input, "((a|b)*abb")
    def test_rejects_input_with_empty_parenthesized_expression(self):
        self.assertRaises(ValueError, validate_input, "()*abb")
    def test_rejects_input_with_invalid_parenthesis_use(self):
        self.assertRaises(ValueError, validate_input, "(*a|b)*abb")
        self.assertRaises(ValueError, validate_input, "(|a|b)*abb")
        self.assertRaises(ValueError, validate_input, "(a|b|)*abb")
    def test_rejects_input_with_invalid_star_use(self):
        self.assertRaises(ValueError, validate_input, "(a|b)|*abb")
        self.assertRaises(ValueError, validate_input, "(a|b)**abb")
        self.assertRaises(ValueError, validate_input, "(a|b)(*abb)")
    def test_rejects_input_with_invalid_union_use(self):
        self.assertRaises(ValueError, validate_input, "a)")
        self.assertRaises(ValueError, validate_input, "(a(|b))*abb")
        self.assertRaises(ValueError, validate_input, "(a||b)*abb")
        self.assertRaises(ValueError, validate_input, "(a|*b)*abb")
        self.assertRaises(ValueError, validate_input, "((a|)b)*abb")
    def test_rejects_input_with_invalid_last_symbol(self):
        self.assertRaises(ValueError, validate_input, "(a|b)*abb(")
        self.assertRaises(ValueError, validate_input, "(a|b)*abb|")
    def test_rejects_input_with_invalid_first_symbol(self):
        self.assertRaises(ValueError, validate_input, "*(a|b)*abb")
        self.assertRaises(ValueError, validate_input, "|(a|b)*abb")



class TestFormatInputForSyntaxTree(unittest.TestCase):
    def test_format_input_for_syntax_tree_adds_concatenation_after_open_parenthesis(self):
        assert format_input_for_syntax_tree("(a|b)a") == "((a|b).a).#"
    def test_format_input_for_syntax_tree_adds_concatenation_after_star_operation(self):
        assert format_input_for_syntax_tree("(a|b)*a") == "((a|b)*.a).#"
    def test_format_input_for_syntax_tree_adds_concatenation_after_alphabet_symbol(self):
        assert format_input_for_syntax_tree("(a|b)abb") == "((a|b).a.b.b).#"