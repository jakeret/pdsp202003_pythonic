import pytest
from pythonic import preprocessing


@pytest.mark.parametrize("top_level_codes, sub_level_codes, expected", [
    (None, None, {}),
    ([], [], {}),
    (["a", "b"], [1, 2], {"a": [1], "b": [2]}),
    (["a", "a"], [1, 2], {"a": [1, 2]}),
])
def test_merge_codes(top_level_codes, sub_level_codes, expected):
    merged_codes = preprocessing.aggregate_codes(top_level_codes,
                                                 sub_level_codes)
    assert merged_codes == expected
