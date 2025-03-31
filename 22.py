def count_non_repeating_elements(lst):
    element_count = {}  
    for num in lst:
        element_count[num] = element_count.get(num, 0) + 1
    non_repeating_count = sum(1 for count in element_count.values() if count == 1)

    return non_repeating_count