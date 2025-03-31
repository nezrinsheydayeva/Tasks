def intersection_of_three(list1, list2, list3):
    set1, set2, set3 = set(list1), set(list2), set(list3)
    return list(set1 & set2 & set3)  