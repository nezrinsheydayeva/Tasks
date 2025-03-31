def rotate_right(lst, k):
    if not lst: 
        return []

    k = k % len(lst)  
    return lst[-k:] + lst[:-k] 
