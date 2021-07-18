"""
Please write a binary search function which searches an item in a sorted list.
The function should return the index of element to be searched in the list.
"""


sorted_list = [1, 3, 6, 7, 8, 9, 12, 17, 21, 22, 24, 27, 30]


def bi_search(sorted_list, start, end, num):
    if (end > start):
        mid = (end + start)//2
        if sorted_list[mid] == num:
            print(mid)
        elif sorted_list[mid] > num:
            end = mid
            bi_search(sorted_list, start, end, num)
        else:
            start = mid + 1
            bi_search(sorted_list, start, end, num)
    else:
        print(-1)


print(bi_search(sorted_list, 0, len(sorted_list) - 1, 8))
