import itertools
import unittest
from typing import Iterator, List, Tuple

from src import solution_02


class TestVerbing(unittest.TestCase):
    def test_add(self):
        strings = ["accept", "commit", "drop", "pay", "set"]
        expected = ["accepting", "commiting", "droping", "paying", "seting"]
        self.assert_multiple(expected, strings)

    def test_replace(self):
        strings = ["accepting", "committing", "dropping", "paying", "setting", "ing"]
        expected = ["acceptly", "committly", "dropply", "payly", "settly", "ly"]

        self.assert_multiple(expected, strings)

    def test_unchanged(self):
        (strings, expected) = itertools.tee(["to", "be", "42", ""])
        self.assert_multiple(expected, strings)

    def assert_multiple(self, expected: Iterator[str], data: Iterator[str]):
        for (expectation, s) in zip(expected, data):
            result = solution_02.verbing(s)
            self.assertEqual(
                expectation,
                result,
                f"verbing('{s}') expected to be '{expectation}' but got '{result}'",
            )


class TestNotBad(unittest.TestCase):
    def test_simple(self):
        data_with_expected = [
            ("", ""),
            ("not", "not"),
            ("bad", "bad"),
            ("not bad", "good"),
            ("notbad", "good"),
            ("bad not", "bad not"),
            ("not substring bad", "good"),
            ("prefix not bad suffix", "prefix good suffix"),
            ("string without the word", "string without the word"),
        ]

        self.assert_multiple(data_with_expected)

    def test_empty(self):
        self.assertEqual("", solution_02.not_bad(""))

    def test_multiple_occurrences(self):
        data_with_expected = [
            ("not not bad", "good"),
            ("not bad bad", "good bad"),
            ("not bad not bad", "good not bad"),
            ("bad not bad not bad", "bad not bad not bad"),
        ]

        self.assert_multiple(data_with_expected)

    def assert_multiple(self, data_with_expected: List[Tuple[str, str]]):
        for (s, expectation) in data_with_expected:
            result = solution_02.not_bad(s)
            self.assertEqual(
                expectation,
                result,
                f"verbing('{s}') expected to be '{expectation}' but got '{result}'",
            )
