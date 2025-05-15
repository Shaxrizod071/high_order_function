def max_task_2_4(w):
    """
    Find the word with the most vowels.
    Args:
        words: list of strings ["tree", "education", "sky", "road"]
    Returns:
        word with most vowels
    """
    def name(s):
        x=0
        for i in s:
            if i in 'aoiue':
                x+=1
        return x
    return (max(w,key=lambda x: name(x)))
print(max_task_2_4(["tree", "education", "sky", "road"]))

