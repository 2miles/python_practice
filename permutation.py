from typing import List


##
# This program generates all permutations of an input list and provides
# additional functionalities to handle duplicate elements and output the
# results either to the console or a file.
#
# The program:
# - Prompts the user for a list input
# - Generates permutations
# - Checks for duplicates, and removes them
# - Optionally writes the results to a file if the input list is longer
#   than four characters.


def generate_permutations(input: List[int]) -> List[List[int]]:
    """
    Generate all permutations of `input`.

    Returns:
    A list of all permutations of the input list.
    """

    result = [[]]
    for i in range(len(input)):
        temp = []
        for elem in result:
            elem.insert(0, input[i])
        j = 0
        while i > 0 and j < factorial(i):
            temp.extend(all_rotations(result[j - 1]))
            j += 1
        result.extend(temp)
    return result


def all_rotations(arr: List[int]) -> List[List[int]]:
    """
    Generate all possible shifted versions of `arr` except the original list.

    Returns:
    A list containing all shifted versions of the input list.
    """
    result = []
    for i in range(1, len(arr)):
        result.append(rotate_list(arr, i))
    return result


def rotate_list(arr: List[int], n: int) -> List[int]:
    """
    Shift the elements of `arr` by to the right by `n` positions.

    Returns:
    The shifted list.
    """
    if n < 0:
        raise ValueError("n must be a positive integer")
    result = [0] * len(arr)
    for i in range(len(arr)):
        result[(i + n) % len(arr)] = arr[i]
    return result


def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def get_list_from_input() -> list:
    """
    Prompts the user for a list input and returns it as a list of characters.

    Returns:
    list: A list of characters parsed from the user's input.
    """
    input_str = input(
        "Enter a list of symbols with no separators or separated by whitespace: "
    )

    # If the input string contains whitespace, split by whitespace.
    if " " in input_str:
        input_list = [item for item in input_str.split()]
    else:
        # If the input string has no whitespace, treat each character as a separate item.
        input_list = list(input_str)
    return input_list


def print_list_elements(input_list: list):
    """
    Prints each element of `input_list` on a new line without any spaces or commas.

    Parameters:
    input_list (list): The list whose elements are to be printed.
    """
    for element in input_list:
        print("".join(map(str, element)))


def write_list_elements_to_file(input_list: list, filename: str):
    """
    Writes each element of `input_list` to a file `filename`, each on a new line without any spaces or commas.
    """
    with open(filename, "w") as file:
        for element in input_list:
            file.write("".join(map(str, element)) + "\n")


def has_duplicates(input_list: list) -> bool:
    """
    Checks if `input_list` contains any duplicate elements.

    Returns:
    True if duplicates are found, False otherwise.
    """
    return len(input_list) != len(set(input_list))


def remove_duplicate_sublists(nested_list: List[List[str]]) -> List[List[str]]:
    """
    Remove duplicate sublists from a nested list while preserving the order of unique sublists.

    Parameters:
    nested_list (List[List[str]]): The nested list from which to remove duplicate sublists.

    Returns:
    List[List[str]]: A new nested list with duplicate sublists removed.
    """
    seen = set()
    unique_nested_list = []

    for sublist in nested_list:
        sublist_tuple = tuple(sublist)
        if sublist_tuple not in seen:
            seen.add(sublist_tuple)
            unique_nested_list.append(sublist)

    return unique_nested_list


if __name__ == "__main__":
    input_list = get_list_from_input()
    result = generate_permutations(input_list)
    print(f"\n{len(result)} total permutations")

    if has_duplicates(input_list):
        old_count = len(result)
        result = remove_duplicate_sublists(result)
        new_count = len(result)
        print(f"{old_count - new_count} duplicates removed")
        print(f"{len(result)} 'unique' permutations of the list:")
    if len(input_list) > 4:
        user_choice = (
            input(
                "The input is longer than 4 characters. Do you want to write the result to a file? (yes/no): "
            )
            .strip()
            .lower()
        )
        if user_choice == "yes":
            filename = input("Enter the filename to write the results to: ").strip()
            write_list_elements_to_file(result, filename)
            print(f"Results have been written to {filename}")
        else:
            print_list_elements(result)
    else:
        print_list_elements(result)
