"""
Python offers an easy way to handle file
Basic Syntax:
for reading:
f = open(filepath, "r")
Get all the text:
    f.read()
Read line by line:
    for line in f
f.close()

for writing:
f = open(filepath, "w")
f.write("in file text")
f.close()

Better Syntax:
Python can handle automatically the opening and the closing of the file by using the context manager with
with open(filepath, mode) as f: # mode can be "r", "w, ....
    code

Exercise 1:
Write a function that takes a filepath as input and print the number of lines in it

Exercise 2:
Write a function that takes a filepath and a list of lines as input and write them in the file
"""


def exercise1(filepath):
    # Put your code here
    pass


def exercise2(filepath, lines):
    # Put your code here
    pass


if __name__ == '__main__':
    import os
    this_folder = os.path.dirname(os.path.abspath(__file__))
    in_filepath = os.path.join(this_folder, "5_file.txt")
    out_filepath = os.path.join(this_folder, "4_file_out.txt")
    LINES = ["line 1", "line 2", "line 3", "line 4", "line 5"]

    print("The expected result for the number of line is 10")
    exercise1(in_filepath)
    exercise2(out_filepath, LINES)


def solution1(filepath):
    count = 0
    with open(filepath, "r") as f:
        for line in f:
            count += 1

    print("The file contains", count, "lines")


def solution2(filepath, lines):
    with open(filepath, "w") as f:
        for line in lines:
            f.write(line + "\n")

