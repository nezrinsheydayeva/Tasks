def remove_duplicates(lst):
    unique_list = [] 
    seen = set()  
    for item in lst:
        if item not in seen:
            unique_list.append(item)  
            seen.add(item)  
    return unique_list