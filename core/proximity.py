# compute closeness of query terms inside one document

def min_distance(pos_list1, pos_list2):
    # find minimum position distance

    i = 0
    j = 0
    best = float("inf")

    while i < len(pos_list1) and j < len(pos_list2):
        p1 = pos_list1[i]
        p2 = pos_list2[j]

        best = min(best, abs(p1 - p2))

        if p1 < p2:
            i += 1
        else:
            j += 1

    return best


def proximity_score(position_lists):
    # compute term proximity score

    if len(position_lists) <= 1:
        return 0  # only one term → no distance

    total = 0

    for i in range(len(position_lists) - 1):
        d = min_distance(position_lists[i], position_lists[i + 1])
        total += d

    return total
