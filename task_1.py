def finder(n, gr):
    max_fives = 0

    if n >= 7:
        left = 0
        fives_count = 0

        for right in range(n):
            if gr[right] == 2 or gr[right] == 3:
                left = right + 1
                fives_count = 0
            elif gr[right] == 5:
                fives_count += 1

            if right - left + 1 == 7:
                max_fives = max(max_fives, fives_count)
                fives_count = 0

            if max_fives == 7:
                return max_fives

    return max_fives if max_fives > 0 else -1


n = int(input())
gr = [int(x) for x in input().split()]
print(finder(n, gr))
