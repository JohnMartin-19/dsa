def remove_duplicates(sequence):
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]

remove_duplicates('peter','Peter','Jmes','James')