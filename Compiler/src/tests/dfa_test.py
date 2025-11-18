import unittest
from dfa import DFA
from syntax_tree import SyntaxTree
from utils import get_postfix, format_input_for_syntax_tree

class TestDFA(unittest.TestCase):
    
    def test_builds_dfa_with_three_states_for_regular_expression_with_single_character(self):
        infix = format_input_for_syntax_tree('a')
        s = SyntaxTree()
        s.build_tree(get_postfix(infix))
        syntax_tree = s.get_tree()
        d = DFA(syntax_tree, sorted(n.number for n in s.root.firstpos))
        dfa = d.build_dfa()

        assert dfa['states'] == [1,2,3]
        assert dfa['alphabet'] == ['a']
        assert dfa['q_0'] == 1
        assert dfa['accepting_states'] == [2]
        assert {'from': 1, 'character': 'a', 'to': 2} in dfa['transitions']
    
    def test_builds_dfa_with_one_state_for_regular_expression_with_single_character_and_star_operation(self):
        infix = format_input_for_syntax_tree('a*')
        s = SyntaxTree()
        s.build_tree(get_postfix(infix))
        syntax_tree = s.get_tree()
        d = DFA(syntax_tree, sorted(n.number for n in s.root.firstpos))
        dfa = d.build_dfa()

        assert dfa['states'] == [1]
        assert dfa['alphabet'] == ['a']
        assert dfa['q_0'] == 1
        assert dfa['accepting_states'] == [1]
        assert {'from': 1, 'character': 'a', 'to': 1} in dfa['transitions']

    def test_builds_dfa_without_epsilon_transitions_for_regular_expression_with_epsilon(self):
        infix = format_input_for_syntax_tree('(a|€)')
        s = SyntaxTree()
        s.build_tree(get_postfix(infix))
        syntax_tree = s.get_tree()
        d = DFA(syntax_tree, sorted(n.number for n in s.root.firstpos))
        dfa = d.build_dfa()

        assert dfa['states'] == [1,2,3]
        assert dfa['alphabet'] == ['a']
        assert dfa['q_0'] == 1
        assert dfa['accepting_states'] == [1,2]
        assert {'from': 1, 'character': 'a', 'to': 2} in dfa['transitions']

    def test_builds_dfa_for_regular_expression_with_only_epsilon(self):
        infix = format_input_for_syntax_tree('€')
        s = SyntaxTree()
        s.build_tree(get_postfix(infix))
        syntax_tree = s.get_tree()
        d = DFA(syntax_tree, sorted(n.number for n in s.root.firstpos))
        dfa = d.build_dfa()

        assert dfa['states'] == [1]
        assert dfa['alphabet'] == []
        assert dfa['q_0'] == 1
        assert dfa['accepting_states'] == [1]
        assert dfa['transitions'] == []


    def test_builds_dfa_for_regular_expression_with_concationation_star_and_union_operations(self):
            infix = format_input_for_syntax_tree('(a|b)*abb')
            s = SyntaxTree()
            s.build_tree(get_postfix(infix))
            syntax_tree = s.get_tree()
            d = DFA(syntax_tree, sorted(n.number for n in s.root.firstpos))
            dfa = d.build_dfa()

            assert dfa['states'] == [1,2,3,4]
            assert dfa['alphabet'] == ['a', 'b']
            assert dfa['q_0'] == 1
            assert dfa['accepting_states'] == [4]
            assert {'from': 1, 'character': 'a', 'to': 2} in dfa['transitions']
            assert {'from': 2, 'character': 'b', 'to': 3} in dfa['transitions']
    
    def test_builds_dfa_for_odd_1s_and_no_leading_zero(self):
            infix = format_input_for_syntax_tree('((2(0|2)*1)|1)(0|2)*(1(0|2)*1(0|2)*)*')
            s = SyntaxTree()
            s.build_tree(get_postfix(infix))
            syntax_tree = s.get_tree()
            d = DFA(syntax_tree, sorted(n.number for n in s.root.firstpos))
            dfa = d.build_dfa()

            assert dfa['states'] == [1,2,3,4,5,6]
            assert dfa['alphabet'] == ['2','0','1']
            assert dfa['q_0'] == 1
            assert dfa['accepting_states'] == [3,5]
            assert {'from': 1, 'character': '0', 'to': 6} in dfa['transitions']
            assert {'from': 6, 'character': '1', 'to': 6} in dfa['transitions']
            assert {'from': 6, 'character': '2', 'to': 6} in dfa['transitions']
            assert {'from': 6, 'character': '0', 'to': 6} in dfa['transitions']
            assert {'from': 1, 'character': '1', 'to': 3} in dfa['transitions']
            assert {'from': 3, 'character': '1', 'to': 4} in dfa['transitions']
            assert {'from': 4, 'character': '1', 'to': 5} in dfa['transitions']
    
    def test_builds_dfa_for_words_without_ba_or_ab(self):
            infix = format_input_for_syntax_tree('c*((a*cc*)|(b*cc*))*(a*|b*)')
            s = SyntaxTree()
            s.build_tree(get_postfix(infix))
            syntax_tree = s.get_tree()
            d = DFA(syntax_tree, sorted(n.number for n in s.root.firstpos))
            dfa = d.build_dfa()

            assert dfa['states'] == [1,2,3,4,5,6,7,8]
            assert dfa['alphabet'] == ['c','a','b']
            assert dfa['q_0'] == 1
            assert dfa['accepting_states'] == [1,2,3,4,5,6,7]
            assert {'from': 1, 'character': 'c', 'to': 2} in dfa['transitions']
            assert {'from': 2, 'character': 'a', 'to': 3} in dfa['transitions']
            assert {'from': 3, 'character': 'b', 'to': 8} in dfa['transitions']
            assert {'from': 2, 'character': 'b', 'to': 6} in dfa['transitions']
            assert {'from': 6, 'character': 'a', 'to': 8} in dfa['transitions']

    def test_builds_dfa_for_even_length_ending_with_0_and_odd_length_ending_with_1(self):
            infix = format_input_for_syntax_tree('(00|01|10|11)*(1|((0|1)0))')
            s = SyntaxTree()
            s.build_tree(get_postfix(infix))
            syntax_tree = s.get_tree()
            d = DFA(syntax_tree, sorted(n.number for n in s.root.firstpos))
            dfa = d.build_dfa()

            assert dfa['states'] == [1,2,3,4]
            assert dfa['alphabet'] == ['0','1']
            assert dfa['q_0'] == 1
            assert dfa['accepting_states'] == [3,4]
            assert {'from': 1, 'character': '1', 'to': 4} in dfa['transitions']
            assert {'from': 4, 'character': '1', 'to': 1} in dfa['transitions']
            assert {'from': 1, 'character': '0', 'to': 2} in dfa['transitions']
            assert {'from': 2, 'character': '0', 'to': 3} in dfa['transitions']
            assert {'from': 4, 'character': '0', 'to': 3} in dfa['transitions']
            assert {'from': 2, 'character': '1', 'to': 1} in dfa['transitions']
            assert {'from': 3, 'character': '0', 'to': 2} in dfa['transitions']
            assert {'from': 3, 'character': '1', 'to': 4} in dfa['transitions']



    



    

