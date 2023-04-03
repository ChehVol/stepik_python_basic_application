import sys
sys.stdin = open("inheritance_in.txt", "r")


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
print(legacy)


def is_parent(p, c):
    if p in legacy[c] or p == c:
        return True
    else:
        for j in legacy[c]:
            if is_parent(p, j) is True:
                return True
    return False


q = int(input())
for i in range(q):
    req = input()
    parent, clas = req.split()
    if is_parent(parent, clas) is True:
        print("Yes")
    else:
        print("No")
