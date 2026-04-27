def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """

    if not isinstance(dct, dict): # Check if dct is a dictionary and raise a TypeError if dct is not a dictionary
        raise TypeError("dct must be a dictionary")

    if key in dct:
        print(f"Original value: {dct[key]}") # If the key already exists in dct, print the original value associated with that key.

    dct[key] = value  # Update the dictionary with the new key-value pair
    return dct


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26
print(update_dictionary({}, "name", "Alice")) # This will add the key-value pair "name": "Alice" to the empty dictionary {} and print the updated dictionary.
print(update_dictionary({"age": 25}, "age", 26)) # This will update the value of the key "age" from 25 to 26 in the dictionary {"age": 25} and print the updated dictionary.