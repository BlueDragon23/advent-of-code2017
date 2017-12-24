

if __name__=="__main__":
    f = open("input9.txt")
    line = f.readline().strip()
    depth = 0
    score = 0
    count = 0
    removed = 0
    cancelled = False
    garbage = False
    for c in line:
        if cancelled:
            cancelled = False
        elif c == '>':
            garbage = False
        elif c == '!':
            cancelled = True
        elif garbage:
            removed += 1
            pass
        elif c == '{':
            depth += 1
        elif c == '}':
            score += depth
            depth -= 1
        elif c == '<':
            garbage = True
        if count < 100:
            print(c, ':', depth, score, cancelled, garbage)
        count += 1

    print(score)
    print(removed)
