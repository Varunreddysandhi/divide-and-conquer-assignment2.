def partition(data, low, high):
    """Partition a section using its last element as the pivot."""

    pivot = data[high]
    boundary = low

    for current in range(low, high):
        if data[current] <= pivot:
            data[boundary], data[current] = (
                data[current], data[boundary]
            )
            boundary += 1

    # Move the pivot into its final sorted position.
    data[boundary], data[high] = data[high], data[boundary]
    return boundary


def quick_sort(data):
    """Sort data in ascending order in place."""

    def sort_section(low, high):
        while low < high:
            pivot_index = partition(data, low, high)

            left_size = pivot_index - low
            right_size = high - pivot_index

            # Recurse on the smaller partition to limit stack usage.
            # Process the larger partition through the loop.
            if left_size < right_size:
                if left_size > 1:
                    sort_section(low, pivot_index - 1)
                low = pivot_index + 1
            else:
                if right_size > 1:
                    sort_section(pivot_index + 1, high)
                high = pivot_index - 1

    sort_section(0, len(data) - 1)