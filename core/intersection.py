# intersect sorted posting lists

def intersect_two_lists(list1, list2):
    # intersect two sorted lists

    i = 0
    j = 0
    result = []

    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            result.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1

    return result

def intersect_many_lists(lists):
    # intersect multiple doc lists

    if not lists:
        return []

    # start with smallest list for efficiency
    lists.sort(key=len)

    result = lists[0]

    for i in range(1, len(lists)):
        result = intersect_two_lists(result, lists[i])
        if not result:
            break

    return result
