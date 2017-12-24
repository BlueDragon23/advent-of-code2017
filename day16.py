import string

def spin(state, n):
    tail = state[n:]
    tail.extend(state[:n])
    return tail

def exchange(state, a, b):
    tmp = state[a]
    state[a] = state[b]
    state[b] = tmp
    return state

def swap(state, a, b):
    x = state.index(a)
    y = state.index(b)
    return exchange(state, x, y)

if __name__=="__main__":
    f = open("input16.txt")
    l = f.readline()
    m = l.strip().split(',')
    state = list(string.ascii_lowercase[:16])
    print(state)
    print(spin(state, -1))
    for _ in range(1000000000):
        for move in m:
            if move[0] == 's':
                state = spin(state, -int(move[1:]))
            elif move[0] == 'x':
                values = move[1:].split('/')
                state = exchange(state, int(values[0]), int(values[1]))
            elif move[0] == 'p':
                values = move[1:].split('/')
                state = swap(state, values[0], values[1])
            else:
                print("You fucked up")
    print(''.join(state))
