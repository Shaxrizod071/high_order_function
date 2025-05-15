def max_task_2_5(people):
    """
    Find the person with the highest age.
    Args:
        people: list of dictionaries [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 45}, {"name": "Tom", "age": 28}]
    Returns:
        dictionary of person with highest age
    """
    asd= filter(lambda x: x["age"]<=100,people)
    return max(asd, key=lambda x: x["age"])
s=max_task_2_5([{"name": "Alice", "age": 30}, {"name": "Bob", "age": 45}, {"name": "Tom", "age": 28}])
print(s)
