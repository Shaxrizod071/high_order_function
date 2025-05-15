def min_task_1_1(numbers):
    """
    Find the smallest number in the list.
    Args:
        numbers: list of integers [3, 1, 4, 2]
    Returns:
        smallest number
    """
    return min(numbers,key=lambda x: x)
print(min_task_1_1([3, 1,4,2]))

