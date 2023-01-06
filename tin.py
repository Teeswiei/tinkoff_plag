from functools import lru_cache


def lev_dist(a, b):
    @lru_cache(None)
    def min_dist(s1, s2):

        if s1 == len(a) or s2 == len(b):
            return len(a) - s1 + len(b) - s2

        if a[s1] == b[s2]:
            return min_dist(s1 + 1, s2 + 1)

        return 1 + min(
            min_dist(s1, s2 + 1),
            min_dist(s1 + 1, s2),
            min_dist(s1 + 1, s2 + 1),
        )

    return min_dist(0, 0)


# нужно ввести
file_name1 = ''
file_name2 = ''
f = open(file_name1, 'r', encoding='UTF-8')
f2 = open(file_name2, 'r', encoding='UTF-8')

w1 = 0
w2 = 0

while True:
    # считываем строку

    line = f.readline()
    line2 = f2.readline()

    w1 += len(line)
    w2 += len(line2)

    # прерываем цикл, если строка пустая
    if not line:
        break
    res += lev_dist(line, line2)
print(res / max(w1, w2))