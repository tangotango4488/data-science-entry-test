def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    # The following line checks if both x and y are instances of int or float. If either x or y is not numeric, the condition will evaluate to True.
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
    
    x, y = y, x # This line swaps the values of x and y in a single statement.
    # Display the values
    print(f"x: {x}, y: {y}") # This should print the swapped values of x and y.
    return

# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17
print(swap("Apple", 10)) # This should return -1 since "Apple" is not numeric.
swap(9, 17) # This should print "x: 17, y: 9" since both 9 and 17 are numeric.
