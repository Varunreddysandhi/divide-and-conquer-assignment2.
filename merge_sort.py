def merge_sort(data):
    """Return a new list containing data in ascending order."""

    # A list with at most one element is already sorted.
    if len(data) <= 1:
        return data.copy()

    # Divide the list and recursively sort both halves.
    middle = len(data) // 2
    left = merge_sort(data[:middle])
    right = merge_sort(data[middle:])

    result = []
    i = 0
    j = 0

    # Merge the two sorted halves.
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any elements remaining in either half.
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result