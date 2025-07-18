# Topic: Lists & Loops

# Sum of All Numbers
# Write a function that takes a list of numbers and returns the sum of all the numbers.

def sum_num(numbers):
    total = 0
    for num in numbers:
        total += num

    return total


# Example usage:
print(sum_num([1, 2, 3, 4, 5]))  # Output: 15


# Count Even Numbers
# Write a function that counts how many even numbers are in a list.

def count_even(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1

    return count


# Example usage:
print(count_even([2, 4, 5, 6, 7, 19, 21])) # Output: 3

# Find Maximum
# Write a function that returns the maximum number in a list.

def max_num(numbers):
    max_val = float('-inf')
    for num in numbers:
        if num > max_val:
            max_val = num

    return max_val

# Example usage:
print(max_num([1, -4, 100, -2])) # Output: 100

# Double Every Number
# Write a function that takes a list and returns a new list where every number is doubled.

def doubled_list(numbers):
    new_list = []
    for num in numbers:
        multiply = num * 2
        new_list.append(multiply)

    return new_list

print(doubled_list([1, 2, 3, 4, 5])) # Output: [2, 4, 6, 8, 10]

# Remove Duplicates
# Write a function that removes duplicates from a list and returns the result.

def remove_duplicates(numbers):
    result = []
    for num in numbers:
        if num not in result:
            result.append(num)

    return result

print(remove_duplicates([1, 1, 1, 3, 4, 6,])) # Output: [1, 3, 4, 6]

def remove_duplicates_optimized(numbers):
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result

print(remove_duplicates_optimized([1, 1, 1, 3, 4, 6,])) # Output: [1, 3, 4, 6]