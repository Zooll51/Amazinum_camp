ball = "B.BB.B.B.B.B.B.BBBBBB.............."


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(buckets):
    m = buckets.count('B')  # Підрахунок кількості символів 'B'
    if m == 0:
        return 0

    n = len(buckets)
    r = -1
    for d in range(2):
        first = d
        last = d + 2 * (m - 1)
        if last >= n:
            break

        may = sum(1 for i in range(first, last + 1, 2) if buckets[i] == 'B')
        r = max(r, may)

        for last in range(last + 2, n, 2):
            may += buckets[last] == 'B'
            may -= buckets[first] == 'B'
            first += 2
            r = max(r, may)

    return r if r < 0 else (m - r)

print(solution(ball))
