def get_even_numbers(input_list):
    return [x for x in input_list if x % 2 == 0]

# Example usage:
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = get_even_numbers(input_list)
print("Even numbers:", even_numbers)
