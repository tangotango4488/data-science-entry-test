def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    i = 0

    while i < len(lst):     # Loop through the list using a while loop
        if lst[i] < 0:      # Check if the current element is negative
            return lst[i]   # Return the first negative number found
        i += 1              # Move to the next index

    return "No negatives"

# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]
print(find_first_negative([3, 5, -1, 7, -2, 8]))  # Expected: -1
print(find_first_negative([2, 10, 7, 0]))         # Expected: "No negatives"