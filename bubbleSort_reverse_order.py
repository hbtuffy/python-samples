def ordered_sequential_search(a_list, item):
    pos = 0
    found = False
    while pos < len(a_list):
        if a_list[pos] == item:
            found = True
            break
        else:
            pos = pos + 1
    return found, pos

def bubbleSort_reverse_order(a_list):
    for i in range(len(a_list) - 1):
        for j in range(len(a_list) - 1):
            if a_list[j] < a_list[j + 1]:
                # Swap elements if they are in the wrong order
                temp = a_list[j]
                a_list[j] = a_list[j + 1]
                a_list[j + 1] = temp

def sort_then_search(a_list, item):
    bubbleSort_reverse_order(a_list)
    return ordered_sequential_search(a_list, item)

def bubbleSort_reverse_order(a_list):
    for i in range(len(a_list) - 1):
        for j in range(len(a_list) - 1):
            if a_list[j] < a_list[j + 1]:
                temp = a_list[j]
                a_list[j] = a_list[j + 1]
                a_list[j + 1] = temp

    return a_list
