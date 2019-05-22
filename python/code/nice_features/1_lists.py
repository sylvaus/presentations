def square(x):
    return x * x


if __name__ == '__main__':
    # Creation
    my_list = [1, 4, 8, 9]

    # Iterate
    print("My list in order")
    for element in my_list:
        print(element)

    # Iterate reversed
    print("My list in reverse order")
    for element in my_list:
        print(element)

    # Iterate with index
    print("My list elements with indexes")
    for index, element in enumerate(my_list):
        print(element, "at index", index)

    # Indexing tricks
    last_element = my_list[-1]
    sub_list = my_list[1:4]  # also works with negative index my_list[1:-2]

    # Generate square values of all the numbers from 0 to 9
    # Programmer way
    my_list = []
    for i in range(0, 10):
        my_list.append(square(i))
    print("l programmer way", my_list)

    # Python programmer way
    my_list = [square(i) for i in range(10)]
    print("l python programmer way", my_list)

    # Functional Python programmer way
    my_list = list(map(square,  range(10)))
    print("l functional python programmer way", my_list)










