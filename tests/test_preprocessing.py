import pytest
from pythonic import preprocessing


@pytest.mark.parametrize("code_a_list, code_b_list, expected", [
    (None, None, {}),
    ([], [], {}),
    (["a", "b"], [1, 2], {"a": [1], "b": [2]}),
    (["a", "a"], [1, 2], {"a": [1, 2]}),
])
def test_merge_codes(code_a_list, code_b_list, expected):
    merged_codes = preprocessing.merge_codes(code_a_list, code_b_list)
    assert merged_codes == expected
