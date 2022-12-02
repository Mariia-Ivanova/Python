def remove_adjacent(lst: list[int]) -> list[int]:
    res = []
    for num in lst:
        if len(res) == 0 or res[-1] != num:
            res.append(num)
    return res


def linear_merge(a: list, b: list) -> list:
    c = []
    ia = 0
    ib = 0
    while ia < len(a) and ib < len(b):
        if a[ia] < b[ib]:
            c.append(a[ia])
            ia += 1
        else:
            c.append(b[ib])
            ib += 1
    c += a[ia:len(a)]
    c += b[ib:len(b)]
    return c

def is_correct(brackets: list[str]) -> bool:
    stack = []
    dict = {'(': ')', '[': ']', '{': '}'}
    for b in brackets:
        if b in '({[':
            stack.append(b)
        if b in ')}]':
            if len(stack) == 0:
                return False
            top = stack.pop()
            if dict[top] != b:
                return False
    return len(stack) == 0
