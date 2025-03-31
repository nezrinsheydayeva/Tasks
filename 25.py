from collections import defaultdict

def count_anagram_groups(words):
    anagram_dict = defaultdict(list)  
    for word in words:
        sorted_word = tuple(sorted(word))  
        anagram_dict[sorted_word].append(word)  
    return len(anagram_dict) 