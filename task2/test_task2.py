import os
import sys
from unittest.mock import patch

import pytest

from task2.task2 import calculate


test_data = [
    (f"task2_test_data/{x}/circle_file.txt", f"task2_test_data/{x}/points_file.txt", f"task2_test_data/{x}/results.txt")
    for x in range(len(os.listdir("task2_test_data")))
]


@pytest.mark.parametrize("circle_filepath, points_filepath, results_filepath", test_data)
def test(circle_filepath: str, points_filepath: str, results_filepath: str):
    with patch.object(sys, "argv", [".\\task2\\task2.py", circle_filepath, points_filepath]), \
            open(results_filepath, 'r') as results_file:
        results = [int(x) for x in results_file.readlines()]
        assert calculate() == results
