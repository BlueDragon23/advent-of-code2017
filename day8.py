from collections import defaultdict
import operator

if __name__=="__main__":
    f = open("input8.txt")
    d = defaultdict(int)
    highest = 0
    for line in f:
        ins, cond = line.strip().split(' if ')
        sub, command, val = ins.split(' ')
        reg, op, comp = cond.split(' ')

        if op == '==':
            op_func = operator.eq
        elif op == '<=':
            op_func = operator.le
        elif op == '>=':
            op_func = operator.ge
        elif op == '!=':
            op_func = operator.ne
        elif op == '<':
            op_func = operator.lt
        elif op == '>':
            op_func = operator.gt
        else:
            print('miss')
            exit(1)
        if op_func(d[reg], int(comp)):
            if command == 'inc':
                d[sub] += int(val)
            else:
                d[sub] -= int(val)
            if d[sub] > highest:
                highest = d[sub]
    vals = list(d.values())
    print(max(vals))
    print(highest)

