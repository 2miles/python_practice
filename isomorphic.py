def is_isomorphic(s1, s2):
    """
    Given two strings `s1`, `s2`, this script determines if they are isomorphic.

    Two strings are isomorphic if the characters in `s1` can be replaced to get `s2`.

    All occurrences of a character must be replaced with another character while
    preserving the order of characters. No two characters may map to the same character,
    but a character may map to itself.

    #### Example 1:

    ```
    Input: s1 = "egg", s2 = "add"
    Output: true
    ```

    #### Example 2:

    ```
    Input: s1 = "foo", s2 = "bar"
    Output: false
    ```

    #### Example 3:

    ```
    Input: s1 = "paper", s2 = "title"
    Output: true
    ```
    """

    mapping = []  # store character mappings
    temp = ()  # temporary store character pairs

    # If the lengths of the two strings are not equal, they cannot be isomorphic
    if len(s1) != len(s2):
        return False

    # Iterate over the characters of both strings, creating a character pair
    # and potentially adding each character pair to the mapping list
    for i in range(len(s1)):
        temp = (s1[i], s2[i])
        if temp in mapping:
            continue

        # Check if the first char of the tuple matches any first char in the mapping list
        # Do the same for the second char, if there is a match there is a conflict.
        first_element_matches = any(temp[0] == pair[0] for pair in mapping)
        second_element_matches = any(temp[1] == pair[1] for pair in mapping)
        if first_element_matches or second_element_matches:
            return False
        else:
            mapping.append(temp)
    # If the loop completes without finding any conflicts, the strings are isomorphic
    return True


if __name__ == "__main__":

    str1 = input("Please enter the first string: ")
    str2 = input("Please enter the second string: ")
    if is_isomorphic(str1, str2):
        print(f"\n'{str1}' and '{str2}' are isomorphic!")
    else:
        print(f"\n'{str1}' and '{str2}' are not isomorphic")
