def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """

    if not isinstance(lst, list): # Check if lst is a list
        return -1

    return [replace_val if x == find_val else x for x in lst] # Use list comprehension to create a new list where each element is replaced with replace_val if it matches find_val, otherwise it remains unchanged.


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"
print(find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)) # This will replace all occurrences of 2 with 5 in the list [1, 2, 3, 4, 2, 2] and print the modified list.
print(find_and_replace(["apple", "banana", "apple"], "apple", "orange")) # This will replace all occurrences of "apple" with "orange" in the list ["apple", "banana", "apple"] and print the modified list.