from collections import defaultdict


def merge_codes(code_a_list, code_b_list):
    if not (code_a_list and code_b_list):
        return {}

    merged_codes = defaultdict(list)
    for code_a, code_b in zip(code_a_list, code_b_list):
        merged_codes[code_a].append(code_b)

    return merged_codes
