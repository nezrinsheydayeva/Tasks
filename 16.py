def flatten_list(nested_list):
    flat_list = [] 

    for item in nested_list:
        if isinstance(item, list):  
            for sub_item in item:
                if isinstance(sub_item, list): 
                    flat_list.extend(sub_item)
                else:
                    flat_list.append(sub_item)
        else:
            flat_list.append(item)

    return flat_list