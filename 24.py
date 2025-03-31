def average_length_unique_strings(strings):
    unique_strings = [s for s in strings if len(s) == len(set(s))]  
    
    if not unique_strings: 
        return 0  

    total_length = sum(len(s) for s in unique_strings)  
    return total_length / len(unique_strings)  