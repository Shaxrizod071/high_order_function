
    """
    return (list(map(lambda x: x[1],p))
)def map_task_3_5(p):
    """
    Extract names from a list of dictionaries.
    Args:
        people: list of dictionaries [{"name": "Alice"}, {"name": "Bob"}, {"name": "Carol"}]
    Returns:
        list of names
    """
    return (list(map(lambda x: x[1],p)))
print(map_task_3_5([{"name": "Alice"}, {"name": "Bob"}, {"name": "Carol"}))
