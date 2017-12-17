def iterate(state, current_pos, val):
    """
    returns next_pos
    """
    next_pos = (current_pos + 316) % len(state)
    state.insert(next_pos + 1, val)
    return next_pos + 1


if __name__=="__main__":
    current_pos = 0
    state = [0]
    for i in range(1, 50000000):
        current_pos = iterate(state, current_pos, i)
    ind = state.index(0)
    print(state[ind:ind+2])
    
