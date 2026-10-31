import csv
import gc
import platform
import random
import statistics
import time
import tracemalloc

from merge_sort import merge_sort
from quick_sort import quick_sort


def run_sort(algorithm, data):
    """Return the sorted result for either algorithm."""
    if algorithm == "Merge Sort":
        return merge_sort(data)

    quick_sort(data)
    return data


def measure_time(algorithm, original, repetitions=5):
    """Return median sorting time in milliseconds."""
    expected = sorted(original)
    times = []

    for _ in range(repetitions):
        # Copying the input is excluded from the measured time.
        working = original.copy()
        gc.collect()

        start = time.perf_counter()
        result = run_sort(algorithm, working)
        elapsed = time.perf_counter() - start

        # Check correctness outside the timed section.
        assert result == expected
        times.append(elapsed * 1000)

    return statistics.median(times)


def measure_memory(algorithm, original):
    """Return peak traced allocations during sorting in KiB."""
    expected = sorted(original)

    # The input copy is created before tracing begins.
    working = original.copy()
    gc.collect()

    tracemalloc.start()
    try:
        result = run_sort(algorithm, working)
        _, peak = tracemalloc.get_traced_memory()
    finally:
        tracemalloc.stop()

    assert result == expected
    return peak / 1024


def main():
    sizes = [100, 250, 500, 1000]
    rng = random.Random(42)
    rows = []

    print("Python:", platform.python_version())
    print("Operating system:", platform.platform())
    print()

    for size in sizes:
        ascending = list(range(size))

        random_data = ascending.copy()
        rng.shuffle(random_data)

        datasets = {
            "Sorted": ascending,
            "Reverse sorted": ascending[::-1],
            "Random": random_data,
        }

        for dataset_name, original in datasets.items():
            for algorithm in ["Merge Sort", "Quick Sort"]:
                median_time = measure_time(algorithm, original)
                peak_memory = measure_memory(algorithm, original)

                rows.append({
                    "Size": size,
                    "Dataset": dataset_name,
                    "Algorithm": algorithm,
                    "Median time (ms)": round(median_time, 6),
                    "Peak traced memory (KiB)": round(peak_memory, 3),
                })

                print(
                    f"{size:>4} | {dataset_name:<14} | "
                    f"{algorithm:<10} | "
                    f"{median_time:.6f} ms | "
                    f"{peak_memory:.3f} KiB"
                )

    with open("results.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    print("\nResults saved to results.csv")


if __name__ == "__main__":
    main()