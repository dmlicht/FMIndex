def find_all(outer, inner):
    """ Find all occurrences of inner in outer """

    next_start = 0
    while True:
        found_index = outer.find(inner, next_start)
        if found_index == -1:
            break
        yield found_index
        next_start = found_index + 1