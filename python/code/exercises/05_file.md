Python offers an easy way to handle file   
Basic Syntax:   
for reading:   
```python
f = open(filepath, "r")

# Get all the text:
f.read()

# Read line by line:
for line in f:
    print(line)

f.close()
```

for writing:
```python
f = open(filepath, "w")
f.write("in file text")
f.close()
```

Better Syntax:    
Python can handle automatically the opening and the closing of the file by using the context manager with
```python
with open(filepath, mode) as f: # mode can be "r", "w, ....
    code
```

Example:
Reading all lines of input.txt
```python
with open("input.txt", "r") as in_file:
    for line in in_file:
        print(line)
```
Writing all elements of my_list in out.txt
```python
my_list = ["abc", "line 2", "line 3"]
with open("out.txt", "w") as out_file:
    for element in my_list:
        out_file.write(element)
```