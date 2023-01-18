import sys
from unittest.mock import patch

import pytest

from task4.task4 import calculate


test_data = [
    ["task4_test_data/data_0", 2],
    ["task4_test_data/data_1", 16],
    ["task4_test_data/data_2", 8],
    ["task4_test_data/data_3", 12],
    ["task4_test_data/data_4", 15],
    ["task4_test_data/data_5", 8]
]


@pytest.mark.parametrize("filepath, result", test_data)
def test(filepath: str, result: int):
    with patch.object(sys, "argv", [".\\task2\\task2.py", filepath]):
        assert calculate() == result
