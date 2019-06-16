"""
Exercise 1:
Fill exercise1 to read all the line in the file defined by the given filepath parameter and count the number of lines
"""


def exercise1(filepath):
    count = 0
    with open(filepath, "r") as f:
        for line in f:
            print(line)
            count += 1

    print("The file contains", count, "lines")


"""
Exercise 2:
Fill exercise2 to write all the line in the lines parameter in the file defined by the given filepath parameter
"""


def exercise2(filepath, lines):
    with open(filepath, "w") as f:
        for line in lines:
            f.write(line)


if __name__ == '__main__':
    import os

    this_folder = os.path.dirname(os.path.abspath(__file__))
    in_filepath = os.path.join(this_folder, "5_file.txt")
    out_filepath = os.path.join(this_folder, "4_file_out.txt")
    LINES = ["line 1\n", "line 2\n", "line 3\n", "line 4\n", "line 5"]

    print("The expected result for the number of line is 10")
    exercise1(in_filepath)
    exercise2(out_filepath, LINES)
