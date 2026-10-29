import calc
import datetime
import os

HISTORY_FILE = "calc_history.txt"

def log_calculation(operation, inputs, result):
    """Log a calculation to the history file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} | {operation}({inputs}) = {result}\n"
    with open(HISTORY_FILE, "a") as f:
        f.write(log_entry)

def average_with_log(numbers):
    """Calculate average and log the operation."""
    result = calc.average(numbers)
    log_calculation("average", numbers, result)
    return result

def multiply_by_two_with_log(number):
    """Multiply by two and log the operation."""
    result = calc.multiply_by_two(number)
    log_calculation("multiply_by_two", number, result)
    return result

def show_history():
    """Display the calculation history."""
    if not os.path.exists(HISTORY_FILE):
        print("No history found.")
        return
    with open(HISTORY_FILE, "r") as f:
        history = f.read()
    if history:
        print("Calculation History:")
        print(history)
    else:
        print("History is empty.")

# Example usage if run directly
if __name__ == "__main__":
    # Perform some calculations
    print("Performing calculations...")
    avg1 = average_with_log([2, 4, 6])
    print(f"Average of [2, 4, 6] = {avg1}")
    
    avg2 = average_with_log([])
    print(f"Average of [] = {avg2}")
    
    mult1 = multiply_by_two_with_log(5)
    print(f"5 * 2 = {mult1}")
    
    mult2 = multiply_by_two_with_log(-3)
    print(f"-3 * 2 = {mult2}")
    
    # Show history
    print("\n" + "="*40)
    show_history()