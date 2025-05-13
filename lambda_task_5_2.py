def lambda_task_5_2(w):
    """
    Sort words by their length (shortest to longest).
    Args:
        words: list of strings ["apple", "banana", "kiwi", "pear"]
    Returns:
        sorted list by word length
    """
    w.sort(key=lambda x: len(x)) 
    return w
print(lambda_task_5_2(['apple','banana','kiwir']))
