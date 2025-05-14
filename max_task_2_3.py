def max_task_1_3(n):
    """
    Find the name with the highest number of letters.
    Args:
        names: list of strings ["Ann", "Robert", "Charlotte", "Mike"]
    Returns:
        name with most letters
    """
    return max(n,key=lambda x: len(x))
print(max_task_1_3(["Ann", "Robert", "Charlotte", "Mike"]))
