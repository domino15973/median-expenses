from datetime import datetime
from statistics import median


def get_first_sunday(year, month):
    """Finds the first Sunday of a given month."""
    first_day = datetime(year, month, 1)
    return 1 + (6 - first_day.weekday()) % 7


def extract_early_expenses(expenses):
    """Extracts expenses up to the first Sunday of each month."""
    early_expenses = []

    for year_month, days in expenses.items():
        year, month = map(int, year_month.split('-'))
        first_sunday = get_first_sunday(year, month)

        for day, categories in days.items():
            if int(day) <= first_sunday:
                for amounts in categories.values():
                    early_expenses.extend(amounts)

    return early_expenses


def solution1(expenses):
    """Naive approach using sorting and median calculation."""
    early_expenses = extract_early_expenses(expenses)
    return median(early_expenses) if early_expenses else None


def quickselect(arr, k):
    """Quickselect algorithm to find the k-th smallest element."""
    low, high = 0, len(arr) - 1

    while low < high:
        mid = (low + high) // 2
        pivot_candidates = [arr[low], arr[mid], arr[high]]
        pivot = sorted(pivot_candidates)[1]

        left, right = low, high

        while left <= right:
            while arr[left] < pivot:
                left += 1
            while arr[right] > pivot:
                right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left, right = left + 1, right - 1

        if k <= right:
            high = right
        elif k >= left:
            low = left
        else:
            return arr[k]

    return arr[low]


def solution2(expenses):
    """
    Optimized approach using Quickselect to find the median in O(n) average time complexity.

    Quickselect is a selection algorithm that, on average, performs in O(n) time. It is efficient for finding
    the median of an unsorted array by partitioning the array iteratively. However, in the worst case (due to poor
    pivot choices), its time complexity can degrade to O(n^2). The space complexity is O(1) as Quickselect
    performs the partitioning in place, requiring no additional data structures.
    """
    early_expenses = extract_early_expenses(expenses)
    if not early_expenses:
        return None

    n = len(early_expenses)
    if n % 2 == 1:
        return quickselect(early_expenses, n // 2)
    else:
        left = quickselect(early_expenses, n // 2 - 1)
        right = quickselect(early_expenses, n // 2)
        return (left + right) / 2
