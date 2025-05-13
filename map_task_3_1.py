def map_task_3_1(n):
    """
    Add 10 to each number.
    Args:
        numbers: list of integers [1, 2, 3]
    Returns:
        list with 10 added to each number
    """
    x=map(lambda x: x+10,n)
    return list(x)
print(map_task_3_1([1,2,3]))
