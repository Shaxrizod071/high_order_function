def filter_task_4_3(n):

    """
    Keep numbers greater than 10.
    Args:
        numbers: list of integers [5, 11, 20, 7, 10]
    Returns:
        list of numbers greater than 10
    """
    n=[5,11,20,7,10]
    a=filter(lambda x: x>=10,n)
    return (list(a))
print(filter_task_4_3(10))

