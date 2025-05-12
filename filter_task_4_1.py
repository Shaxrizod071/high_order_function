def filter_task_4_1(n):
    """
    Filter out even numbers.
    Args:
        numbers: list of integers [1, 2, 3, 4, 5]
    Returns:
        list of odd numbers
    """
    n=[1,2,3,4,5,6,7,8,9,10]
    a=filter(lambda n: n%2==1,n)
    return list(a)
print(filter_task_4_1(10)) 
