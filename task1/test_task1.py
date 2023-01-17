import sys
from unittest.mock import patch

import pytest

from task1.task1 import find_path


test_data = [
    (4, 3, "13"),
    (5, 4, "14253"),
    (1, 1, "1"),
    (3, 3, "132"),
    (5, 5, "15432"),
    (10, 10, "11098765432"),
    (10, 11, "1"),
    (10, 12, "12345678910"),
    (4, 7, "13")
]


@pytest.mark.parametrize("n, m, result", test_data)
def test(n: int, m: int, result: str):
    with patch.object(sys, "argv", [".\\task1\\task1.py", str(n), str(m)]):
        assert find_path() == result
