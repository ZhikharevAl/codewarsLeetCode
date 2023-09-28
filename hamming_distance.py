def hamming_distance(message1, message2):
    if len(message1) != len(message2):
        return -1
    else:
        return sum(el1 != el2 for el1, el2 in zip(message1, message2))


# Test the function
message1 = "karolin"
message2 = "kathrin"
result = hamming_distance(message1, message2)
print(result)
