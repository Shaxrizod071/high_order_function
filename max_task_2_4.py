def max_task_2_4(w):
    """
    Find the word with the most vowels.
    Args:
        words: list of strings ["tree", "education", "sky", "road"]
    Returns:
        word with most vowels
    """
    if w in 'aieuo':
         return True
    else:
        return False
print(max_task_2_4(["tree", "education", "sky", "road"]))

