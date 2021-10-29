def duplicate_count(text):
    
    # make all lower case
    text_small = text.lower()
    
    # initialize counter
    counter = {}
    
    # loop through all letters and sum up number of occurance
    for t in text_small:
        counter[t] = counter.get(t, 0) + 1
    
    # keep only those with a count of >= 2
    duplicates = []
    for k in counter:
        if counter[k] >= 2:
            duplicates.append(k)
    
    # return number of >= 2 counts
    return len(duplicates)
    

