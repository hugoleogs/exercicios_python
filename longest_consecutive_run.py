def longest_run(lst):
    qtt = 1
    hist = 0
    falha = 0
    lst.sort()
    for (y, x) in enumerate(lst[:-1]):
        if (x + 1) == lst[y + 1]:
            if falha == 1:
                if hist <= qtt:
                    hist = qtt
                falha = 0
                qtt = 1
            qtt += 1

        elif (x) == lst[y + 1]:
            pass
        else:
            falha = 1

    return max([qtt, hist])


print(longest_run([1, 2, 3, 5, 6, 7, 8, 9]))
print(longest_run([1, 2, 3, 10, 11, 15]))
print(longest_run([-7, -6, -5, -4, -3, -2, -1]))
print(longest_run([3, 5, 6, 10, 15]))
print(longest_run([3, 5, 7, 10, 15]))
print(longest_run([5, 4, 3, 2, 1]))
print(longest_run([5, 4, 2, 1]))
print(longest_run([10, 9, 0, 5]))
print(longest_run([1, 2, 3, 2, 1]))
print(longest_run([10, 9, 8, 7, 6, 2, 1]))