import os
import statistics

class FileNotFoundCustomError(Exception):
    pass

def calculate_average(marks):
    return statistics.mean(marks)

def highest_mark(marks):
    return max(marks)

def lowest_mark(marks):
    return min(marks)

def read_marks(filename):
    if not os.path.exists(filename):
        raise FileNotFoundCustomError(f"File {filename} not found")
    with open(filename, 'r') as f:
        data = f.read().strip()
        marks = list(map(int, data.split()))
    return marks

# main.py
from assingment import read_marks, calculate_average, highest_mark, lowest_mark

marks = read_marks("marks.txt")
print(f"Average: {calculate_average(marks)}")
print(f"Highest: {highest_mark(marks)}")
print(f"Lowest: {lowest_mark(marks)}")