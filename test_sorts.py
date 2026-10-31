from merge_sort import merge_sort
from quick_sort import quick_sort


test_cases = [
    [],
    [7],
    [8, 3, 5, 2],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [4, 2, 4, 1, 2],
    [-3, 0, 5, -1],
]

for original in test_cases:
    expected = sorted(original)

    # Merge Sort returns a new list.
    merge_input = original.copy()
    merge_result = merge_sort(merge_input)

    assert merge_result == expected
    assert merge_input == original

    # Quick Sort changes the supplied list.
    quick_result = original.copy()
    quick_sort(quick_result)

    assert quick_result == expected

print("All sorting tests passed.")