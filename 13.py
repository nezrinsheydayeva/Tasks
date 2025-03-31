def most_frequent_element(lst):
    frequency = {} 
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1

   
    most_frequent = None
    max_count = 0

    for key, count in frequency.items():
        if count > max_count:
            most_frequent = key
            max_count = count

    return most_frequent
