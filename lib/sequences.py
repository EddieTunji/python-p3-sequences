def print_fibonacci(length):
    sequence = []

    if length == 0:
        print(sequence)
        return
    elif length == 1:
        sequence = [0]
    else:
        sequence = [0, 1]
        while len(sequence) < length:
            next_value = sequence[-1] + sequence[-2]
            sequence.append(next_value)

    print(sequence)
