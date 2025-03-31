def find_second_largest(nums):
    if len(nums) < 2:
        return "List must contain at least two numbers."

    largest = second_largest = float('-inf')  

    for num in nums:
        if num > largest:
            second_largest = largest 
            largest = num  
        elif num > second_largest and num != largest:
            second_largest = num 

    return second_largest if second_largest != float('-inf') else "No second largest number found."
