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

# Double Every Number
# Write a function that takes a list and returns a new list where every number is doubled.

# Remove Duplicates
# Write a function that removes duplicates from a list and returns the result.