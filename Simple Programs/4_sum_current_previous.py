# Write a Python code to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

current = 0
previous = 0
Sum = 0

print("Printing current and previous number and their sum in a range(10)")
for i in range(10):
    if i == 0:
        Sum = 0
        print(f"Current Number {current} Previous Number {previous} Sum: {Sum}")
    else:
        previous = i - 1
        current = i
        Sum = previous + current
        print(f"Current Number {current} Previous Number {previous} Sum: {Sum}")

current = 0
previous = 0
Sum = 0

print("Printing current and previous number and their sum in a range(10)")
for i in range(10):
    print(f"Current Number {current} Previous Number {previous} Sum: {Sum}")
    previous = current
    current = i + 1
    Sum = current + previous