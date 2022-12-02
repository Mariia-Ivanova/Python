import unittest
import os

from src.tests import utils

this_path = os.path.realpath(__file__)
solution_path = os.path.normpath(os.path.join(this_path, "../../solution_05.py"))
# Change it if you run your scripts not with 'python3' command
python_executable_name = "python3"
run_cmd = [python_executable_name, solution_path]


class TestWc(unittest.TestCase):
    def test_one_file(self):
        self.run_and_compare_with_wc("111 222\n333")

    def test_one_line(self):
        self.run_and_compare_with_wc("aaaaaaaaaaaaaaaaaaa")

    def test_multiple_files(self):
        self.run_and_compare_with_wc("1\n2 3", "3\n4\n5", "42")

    def test_non_unicode(self):
        self.run_and_compare_with_wc("Привет, мир!")

    def test_a_lot_whitespaces(self):
        self.run_and_compare_with_wc("\n\n\n\n\n\n\n")

    def run_and_compare_with_wc(self, *args: str):
        out, fn = utils.run_script(run_cmd, *args)
        expected, _ = utils.run_script(["wc"], *args, file_names=fn)

        self.assertEqual(expected, out)
