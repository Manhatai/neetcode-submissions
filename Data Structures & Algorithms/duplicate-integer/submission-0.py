numbers1 = [1, 2, 3, 3]
numbers2 = [1, 2, 3, 4]

def areThereDuplicates(list):
    for x in range(len(list)):
        for y in range(x + 1, len(list)):
            if list[x] == list[y]:
                return True
    return False
            