import json
import sys
from typing import Dict, Iterable, List, Union


def get_args() -> Iterable:
    args = [x for x in sys.argv[1:]]
    return args


def set_result(values: Dict[int, str], test: Dict[str, Union[int, str]]) -> dict:
    if "value" in test:
        test["value"] = values[test["id"]]
    if "values" in test:
        for child_test in test["values"]:
            set_result(values, child_test)
    return test


def prepare_results() -> Dict[str, List[Dict[str, Union[int, str]]]]:
    tests_filepath, values_filepath = get_args()
    with open(tests_filepath, 'r') as tests_file, open(values_filepath, 'r') as values_file:
        tests = json.load(tests_file)["tests"]
        # {id: result}
        values = {result["id"]: result["value"] for result in json.load(values_file)["values"]}
        results = []
        for test in tests:
            results.append(set_result(values, test))
    return {"tests": results}


if __name__ == "__main__":
    with open("report.json", 'w') as report_file:
        json.dump(prepare_results(), report_file)
