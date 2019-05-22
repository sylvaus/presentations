import os

# Get the absolute path of the folder in which this file is
THIS_FILE_DIRPATH = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    # Open and read a file the old way
    f = open("hello.txt", "r")
    print("The file contains:", f.read())
    f.close()

    # The Python way
    with open("hello.txt", "r") as f:
        print(f.read())

    # Iterates through lines
    with open("hellos.txt", "r") as f:
        i = 1
        for line in f:
            # Strip is needed to remove the \n at the end of the line
            print("Line", i, ":", line.strip())
            i += 1

