# Project-10

## Simple Calculator

A command-line calculator that performs basic arithmetic operations with the ability to chain calculations using previous results.

## Features

- Four basic operations: addition, subtraction, multiplication, division
- Continue calculating with previous results
- Start fresh calculations at any time
- Function dictionary mapping for operation selection

## Requirements

No external dependencies required. Uses Python standard library only.

## Usage

Run the program:
```bash
python calculator.py
```

Follow the prompts:
1. Enter your first number
2. Select an operation (+, -, *, /)
3. Enter your second number
4. View the result
5. Choose to continue with the result or start a new calculation

## How It Works

The program uses a dictionary to map operator symbols to their corresponding functions. Users can chain calculations by using the previous result as the first number in subsequent operations, or restart with fresh numbers.

## Example Output
```
What is your first number? 10
+
-
*
/
Pick an operation: +
What is your second number? 5
10.0 + 5.0 = 15.0
Type 'y' to continue calculating with 15.0, or type 'n' to start a new calculation: y
+
-
*
/
Pick an operation: *
What is your second number? 2
15.0 * 2.0 = 30.0
Type 'y' to continue calculating with 30.0, or type 'n' to start a new calculation: n
```

## What I Learned

- **First-class functions**: Storing functions as dictionary values for dynamic operation selection
- **Nested loops**: Using inner and outer loops to control calculation flow and program continuation
- **Function composition**: Creating a `calculate()` function that calls other functions based on conditions
- **State management**: Maintaining and updating the first number with previous results for chained calculations
- **User flow design**: Building an intuitive continue/restart workflow for better user experience
- **Type conversion**: Using `float()` to handle both integer and decimal inputs
