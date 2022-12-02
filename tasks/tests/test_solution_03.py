import os
import unittest

from tests import utils

this_path = os.path.realpath(__file__)
solution_path = os.path.normpath(os.path.join(this_path, "../../solution_03.py"))
# Change it if you run your scripts not with 'python3' command
python_executable_name = "python3"


class TestDictionary(unittest.TestCase):
    def test_readme(self):
        data = """
apple - malum, pomum, popula
fruit - baca, bacca, popum
punishment - malum, multa
        """.strip()
        expected = (
            "baca - fruit\n"
            "bacca - fruit\n"
            "malum - apple, punishment\n"
            "multa - punishment\n"
            "pomum - apple\n"
            "popula - apple\n"
            "popum - fruit\n"
        )

        out, _ = utils.run_script([python_executable_name, solution_path], data)

        self.assertEqual(expected, out)
