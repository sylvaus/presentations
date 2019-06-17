Python offers two keywords for looping
while and for

Syntax:  
```Python 
for element in elements:   
    code

while condition:
    code
```

You can also break from a loop using the break keyword

Examples
```Python
my_list = [10, 45, 78]
for elt in my_list:
    print(elt)
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

for elt in my_list:
    if elt == 45:
        break
# will print 
# 0 10 

index = 0
while index < len(my_list):
    print(my_list[index])
# will print 
# 10 
# 45 
# 78



