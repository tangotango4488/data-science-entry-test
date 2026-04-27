def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    if not isinstance(s, str): # Check if the input is a string and raise an error if the input is not a string
        raise TypeError("Input must be a string")
    
    return s[::-1] # Reverse the string using slicing and return the reversed string


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"
print(string_reverse("Hello World")) # Expected output: "dlroW olleH"
print(string_reverse("Python")) # Expected output: "nohtyP"