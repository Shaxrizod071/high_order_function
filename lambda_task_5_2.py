def lambda_task_5_2(w):
    """
    Sort words by their length (shortest to longest).
    Args:
        words: list of strings ["apple", "banana", "kiwi", "pear"]
    Returns:
        sorted list by word length
    """
    w=["apple","banana","kiwi","pear"]
    a=(lambda x: x.sort() if len(x)>=2 else x ,w)
    return (list(a)
print(lambda_task_5_2(banana))
