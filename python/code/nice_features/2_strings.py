if __name__ == '__main__':
    # Useful commands
    # Splitting
    csv_elements = "a,b,c,d"
    elements = csv_elements.split(",")
    print("The elements of", csv_elements, "are:", elements)

    # Substitution (replacing)
    text_with_typo = "This is corrrext"
    text_corrected = text_with_typo.replace("corrrext", "correct")
    print("Before:", text_with_typo, ", after:", text_corrected)

    # Checks if sub_string in string
    sub_string = "abc"
    string = "1abcdef"
    print(sub_string, "is in", string, ":", sub_string in string)

    # Checks if string starts/ends with sub_string
    sub_string = "abc"
    string = "abcdef"
    print(string, "starts with", sub_string, ":", string.startswith(sub_string))
    print(string, "ends with", sub_string, ":", string.endswith(sub_string))

    # Formatting text
    print("Today, I learnt about {} version {}.{}".format("Python", 3, "X"))

    # Removing the leading and trailing whitespace and \n
    string = "     a lot of space before and after       "
    print("Text will be stripped of its leading and trailing space")
    print("START{}END".format(string.strip()))

    # Comparison
    string = "abS"
    string2 = "ABS"

    print(string, "equals to", string2, ":", string == string2)
    # Python 3
    print(string, "equals to", string2, "if the case is ignored:", string.casefold() == string2.casefold())
    # Python 2
    print(string, "equals to", string2, "if the case is ignored:", string.lower() == string2.lower())

    # Concatenate strings
    groceries = ["milk", "bread", "toasts"]
    print("I need " + " and ".join(groceries))
