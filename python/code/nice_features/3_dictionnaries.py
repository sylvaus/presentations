from collections import defaultdict, OrderedDict


def print_input(text):
    print("Input is", text)


def print_func(text):
    print("Func is", text)


def standard_dict():
    # Instantiation
    d = {}
    # Or with values
    d_full = {
        1: "Number 1"
        , 2: "Number 2"
        , "3": "Number 3"
    }

    # Accessing values
    print(d_full[1], d_full[2], d_full["3"])
    
    print(d_full.get(1, ))


def default_dict():
    arr = [1, 2, 2, 3, 4]
    d = defaultdict(int)
    for elt in arr:
        d[elt] += 1

    print(d)


def ordered_dict():
    d = OrderedDict([
        ("Input", print_input),
        ("Func", print_func)
    ])
    for key in d.keys():
        if key in "Input_Func_3":
            d[key]("Input_Func_3")
            break


if __name__ == '__main__':
    standard_dict()
    default_dict()
    ordered_dict()




