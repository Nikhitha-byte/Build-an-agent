def average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

def multiply_by_two(number):
    """Return the number multiplied by 2."""
    return number * 2

print(average([2, 4, 6]))
print(average([]))
print(f"The result of multiplying 5 by 2 is {multiply_by_two(5)}")
print(f"The result of multiplying -3 by 2 is {multiply_by_two(-3)}")
