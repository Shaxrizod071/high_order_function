def map_task_3_2(w):
    """
    Convert all words to uppercase.
    Args:
        words: list of strings ["cat", "dog", "fish"]
    Returns:
        list of uppercase words
    """
    x=map(lambda x: x.title(),w)
    return list(x)
print(map_task_3_2(["cat","dog"]))
