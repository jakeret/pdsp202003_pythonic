from collections import defaultdict
from typing import List, Dict


def aggregate_codes(top_level_codes: List, sub_level_codes: List) -> Dict:
    if not (top_level_codes and sub_level_codes):
        return {}

    merged_codes = defaultdict(list)
    for code_a, code_b in zip(top_level_codes, sub_level_codes):
        merged_codes[code_a].append(code_b)

    return merged_codes
