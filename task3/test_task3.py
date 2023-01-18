import json
import sys
from unittest.mock import patch
from task3.task3 import prepare_results


def test():
    argv = [".\\task3\\task3.py", "task3_test_data/tests.json", "task3_test_data/values.json"]
    with patch.object(sys, "argv", argv), open("task3_test_data/report.json", 'r') as report_file:
        report = json.load(report_file)
        assert prepare_results() == report
