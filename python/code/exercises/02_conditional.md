Python offers three conditions keyword: if elif and else  
Syntax:   
```python
if condition:
    code
elif condition: # combination of else and if
    code
else:
    condition
```

You always need `if` but `elif` and `else` 

Example:
```python
nb = 1245
if nb > 10000:
    print("big number")
elif nb > 100:
    print("medium number")
else:
    print("small number") 
```