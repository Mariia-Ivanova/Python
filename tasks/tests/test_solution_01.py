import unittest

from src import solution_01


class TestRemoveAdjacent(unittest.TestCase):
    def test_simple(self):
        lst = [1, 1, 2, 2, 3, 3]
        result = solution_01.remove_adjacent(lst)
        self.assertListEqual([1, 2, 3], result)

    def test_unique(self):
        lst = [1, 2, 3]
        result = solution_01.remove_adjacent(lst)
        self.assertListEqual(lst, result)

    def test_new_list(self):
        lst = []
        result = solution_01.remove_adjacent(lst)
        self.assertIsNot(lst, result)

    def test_not_mutates(self):
        lst = [1, 1, 1]
        solution_01.remove_adjacent(lst)
        self.assertListEqual([1, 1, 1], lst)


class TestLinearMerge(unittest.TestCase):
    def test_simple(self):
        a = [1, 3, 5]
        b = [2, 4, 6]
        result = solution_01.linear_merge(a, b)
        self.assertListEqual([1, 2, 3, 4, 5, 6], result)

    def test_empty(self):
        a = [1, 2, 3]
        b = []

        result = solution_01.linear_merge(a, b)
        self.assertListEqual([1, 2, 3], result)

        result = solution_01.linear_merge(b, a)
        self.assertListEqual([1, 2, 3], result)

    def test_different_len(self):
        a = [1, 3, 5]
        b = [2, 4, 6, 7, 8, 9]
        result = solution_01.linear_merge(a, b)
        self.assertListEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], result)

    def test_sequential(self):
        a = [1, 2, 3]
        b = [4, 5, 6]
        result = solution_01.linear_merge(a, b)
        self.assertListEqual([1, 2, 3, 4, 5, 6], result)

        result = solution_01.linear_merge(b, a)
        self.assertListEqual([1, 2, 3, 4, 5, 6], result)

    def test_pure(self):
        a = [1, 3, 5]
        b = [2, 4, 6]
        solution_01.linear_merge(a, b)
        self.assertListEqual([1, 3, 5], a)
        self.assertListEqual([2, 4, 6], b)


class TestIsCorrect(unittest.TestCase):
    def test_simple(self):
        brackets = list("(())()")
        self.assertTrue(solution_01.is_correct(brackets))

    def test_empty(self):
        self.assertTrue(solution_01.is_correct([]))

    def test_different_brackets(self):
        brackets = list("{}()[]({[]})")
        self.assertTrue(solution_01.is_correct(brackets))

    def test_incorrect(self):
        incorrect_sequences = [list("(]"), list("("), list("}"), list("(())[")]

        for brackets in incorrect_sequences:
            self.assertFalse(
                solution_01.is_correct(brackets),
                f"Bracket sequence '{brackets}' is incorrect but pass the check",
            )
