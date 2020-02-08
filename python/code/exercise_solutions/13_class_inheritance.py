"""
Exercise 1

Write a CSVReader class which inherits from the FileReader class,
CSVReader should have a constructor that takes as inputs the csv filepath and the delimiter for the csv
CSVReader should also override read_line to return the elements of the line instead of the line.
For example, if the line is "a,b,c,d" and the delimiter is "," then the list ["a,"b","c","d"] should be returned
"""


class FileReader:
    def __init__(self, filepath):
        self._lines = []
        with open(filepath, "r") as f:
            self._lines = f.read().splitlines(keepends=False)

        self._line_index = 1

    @property
    def line_index(self):
        return self._line_index

    @property
    def nb_of_lines(self):
        return len(self._lines)

    def reset(self):
        self._line_index = 1

    def goto_line(self, line_index):
        if line_index < 1:
            raise ValueError("Line index cannot be smaller than 1")
        if line_index > self.nb_of_lines:
            raise ValueError("Line index cannot be bigger than the number of lines {}".format(self.nb_of_lines))
        self._line_index = line_index

    def read_line(self):
        return self._lines[self._line_index - 1]

    def has_next_line(self):
        if self._line_index >= self.nb_of_lines:
            return False
        return True

    def read_next_line(self):
        self._line_index += 1
        return self.read_line()


class CSVReader(FileReader):
    def __init__(self, filepath, separator=","):
        super().__init__(filepath)
        self._separator = separator

    def read_line(self):
        return self._lines[self._line_index - 1].split(self._separator)


# Example of FileReader Usage
if __name__ == '__main__':
    file_reader = FileReader("05_file.csv")
    print(file_reader.read_line())
    while file_reader.has_next_line():
        print(file_reader.read_next_line())
