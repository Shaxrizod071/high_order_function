def max_task_2_2(w):
    """
    Find the longest word.
    Args:
        words: list of strings ["pen", "notebook", "eraser"]
    Returns:
        longest word
    """
    return max(w,key=lambda x: len(x))
print(max_task_2_2(["pen", "notebook", "eraser"]))
