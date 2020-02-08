Python offers two keywords for looping
while and for

Syntax:  
```Python 
for element in elements:   
    code

while condition:
    code
```

Examples
```Python
my_list = [10, 45, 78]
for elt in my_list:
    print(elt)
# will print 
# 10 
# 45 
# 78

index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1
# will print 
# 10 
# 45 
# 78

# If you need the index, use enumerate. 
# enumerate(my_list) returns a pairs of index, element 
for index, elt in enumerate(my_list):
    print(index, elt)
# will print 
# 0 10 
# 1 45 
# 2 78    

# Interrupting a for/while loop can be done by using the break keyword
for elt in my_list:
    if elt == 45:
        break
# will print 
# 0 10 

index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1
# will print 
# 0 10 
```


