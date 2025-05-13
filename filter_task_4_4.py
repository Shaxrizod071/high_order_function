def filter_task_4_4(n):
    """
    Filter names that start with "A".
    Args:
        names: list of strings ["Alice", "Bob", "Anna", "Charlie"]
    Returns:
        list of names that start with "A"
    """
    s=filter(lambda x: True if x[0]=='A' or x[0]=='a' else False,n)
    return list(s)
print(filter_task_4_4("Alice"))
