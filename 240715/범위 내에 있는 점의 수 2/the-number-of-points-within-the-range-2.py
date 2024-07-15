MAX_RANGE = 1000000


def get_sum(s, e, lines):
    return lines[e] - lines[s-1]


if __name__ == "__main__":
    n, q = map(int, input().split())
    dots = list(map(int, input().split()))
    lines = [0] * (MAX_RANGE+1)
    for dot in dots:
        lines[dot] = 1

    for i in range(1, MAX_RANGE+1):
        lines[i] = lines[i-1] + lines[i]

    for _ in range(q):
        s, e = map(int, input().split())
        print(get_sum(s, e, lines))