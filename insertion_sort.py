case1 = [4, 2, 1, 3]
case2 = [-1, 5, 3, 4, 0]


def insertion_sort(head: list):
    for x in range(1, len(head)):
        current_index = x
        comparison_index = x-1
        while head[current_index] < head[comparison_index] and current_index > 0:
            head[current_index], head[comparison_index] = head[comparison_index], head[current_index]
            comparison_index -= 1
            current_index -= 1
    return head


print(insertion_sort(case1))
print(insertion_sort(case2))
