def filter_task_4_4(n):
    """
    Filter names that start with "A".
    Args:
        names: list of strings ["Alice", "Bob", "Anna", "Charlie"]
    Returns:
        list of names that start with "A"
    """
    return n[0]
    n=["Alice","Bob","Anna","Charline"]
    s=filter(lambda x: x[0] if x[0]==A or x[0]==a else n,n)
    return list(s)
print(filter_task_4_4("Alice"))
