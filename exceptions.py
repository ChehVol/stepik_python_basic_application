import sys
sys.stdin = open("exceptions_in.txt", "r")


def create_legacy():
    n = int(input())
    lst = {}
    for i in range(n):
        line = input()
        if ":" in line:
            child, parents = line.split(' :')
            lst[child] = parents.split()
        else:
            lst[line] = []
    return lst


legacy = create_legacy()


def is_parent(p, c):
    if p in legacy[c] or p == c:
        return True
    else:
        for j in legacy[c]:
            if is_parent(p, j) is True:
                return True
    return False


m = int(input())
exceptions = []
for i in range(m):
    exc = input()
    for j in exceptions:
        if is_parent(j, exc) is True:
            print(exc)
            break
    exceptions.append(exc)
