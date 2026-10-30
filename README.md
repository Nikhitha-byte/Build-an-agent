# Build an Agent - Calculator Project

This project demonstrates a simple calculator with history tracking, featuring both a Python backend and a frontend HTML interface.

## Features

- **Average Calculation**: Computes the average of a list of numbers, handling empty lists gracefully.
- **Multiplication by 2**: Multiplies a given number by 2.
- **History Tracking**: Logs all calculations with timestamps to a text file.
- **Interactive HTML Interface**: A user-friendly web interface for performing calculations and viewing history.

## Files

- `calc.py`: Contains the core calculator functions (`average` and `multiply_by_two`).
- `calc_history.py`: Extends the calculator functions with history logging and provides a history display function.
- `calculator.html`: An interactive HTML/JavaScript calculator interface with real-time results and history tracking.
- `server.py`: A simple Python HTTP server to serve the calculator HTML file (optional).
- `calc_history.txt`: Log file that stores the calculation history (generated automatically).

## Usage

### Using the Python Functions

You can use the calculator functions directly in Python:

```python
import calc

# Calculate average
print(calc.average([2, 4, 6]))  # Output: 4.0
print(calc.average([]))         # Output: None

# Multiply by 2
print(calc.multiply_by_two(5))  # Output: 10
print(calc.multiply_by_two(-3)) # Output: -6
```

### Using the History Tracking Functions

```python
import calc_history

# Perform calculations with logging
avg = calc_history.average_with_log([2, 4, 6])
print(f"Average: {avg}")

result = calc_history.multiply_by_two_with_log(5)
print(f"Multiplication result: {result}")

# View history
calc_history.show_history()
```

### Using the HTML Interface

1. Open `calculator.html` in any web browser (double-click the file or right-click -> "Open with").
2. Alternatively, run the server:
   ```bash
   python server.py
   ```
   Then open your browser to `http://localhost:8000`.

3. Select an operation from the dropdown:
   - **Calculate Average**: Enter comma-separated numbers (e.g., "2,4,6")
   - **Multiply by 2**: Enter a single number
4. Click "Calculate" to see the result.
5. View your calculation history below the result.

## Requirements

- Python 3.x (for the Python scripts and server)
- Any modern web browser (for the HTML interface)

## How It Works

### Backend (Python)

The `calc.py` module provides basic mathematical operations:
- `average(numbers)`: Returns the arithmetic mean or `None` for empty lists.
- `multiply_by_two(number)`: Returns the input multiplied by 2.

The `calc_history.py` module wraps these functions to add logging:
- Each calculation is logged with a timestamp to `calc_history.txt`.
- The `show_history()` function reads and displays the log file.

### Frontend (HTML/JavaScript)

The `calculator.html` file provides an interactive interface:
- Uses vanilla JavaScript (no frameworks required).
- Dynamically shows/hides input fields based on the selected operation.
- Performs calculations client-side for instant feedback.
- Maintains a history of calculations in the browser session.
- Updates the history display after each calculation.

## Example Calculations

**Average:**
- Input: `2,4,6` → Output: `4.0`
- Input: `10,20,30,40` → Output: `25.0`
- Input: (empty) → Output: `None` (displayed in red)

**Multiply by 2:**
- Input: `5` → Output: `10`
- Input: `-3` → Output: `-6`
- Input: `0` → Output: `0`

## Extending the Project

To add more operations:
1. Add the function to `calc.py`.
2. Add a corresponding wrapper function in `calc_history.py` that logs the operation.
3. Update the HTML interface to include the new operation in the dropdown and add the necessary input fields and calculation logic.

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Created as part of the "Build an agent" project.
- Uses standard web technologies (HTML5, CSS3, JavaScript ES6).