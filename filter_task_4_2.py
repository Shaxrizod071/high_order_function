def filter_task_4_2(w):
    """
    Keep words longer than 4 letters.
    Args:
        words: list of strings ["hi", "hello", "world", "cat"]
    Returns:
        list of words longer than 4 letters
    """
  
    w=["hi","hello","world","cat"]
    a=filter(lambda x: x[4:] if len(x)>=4 else [],w) 
    return (list(a))
print(filter_task_4_2('hello'))
