def get_digits_count(message):
    return sum([int(i) for i in message if i.isdigit()])
