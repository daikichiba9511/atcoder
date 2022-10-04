N = int(input())


def is_valid_bracket(s: str) -> bool:
    depth = 0
    for s_i in s:
        if s_i == "(":
            depth += 1
        if s_i == ")":
            depth -= 1

        if depth < 0:
            return False

    if depth:
        return False
    return True


# 1 <= N <= 20
# O(N2^N) \approx 10 ^ 7
for i in range(2 ** N):
    candidate = ""
    # N個の並びのうち上の桁数から見てくからN-1からはじめる
    for j in range(N - 1, -1, -1):
        # iのj bit目が0で有るための条件
        if i & (1 << j) == 0:
            candidate += "("
        else:
            candidate += ")"

    if is_valid_bracket(candidate):
        print(candidate)
