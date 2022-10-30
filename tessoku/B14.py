import bisect

# 前半N/2と後半N/2のありえる組み合わせを調べる
# 1 <= N <= 30
# O(2 ** 15) = 10 ^ 5
# 半分全列挙


def enumerated_summations(l):
    """lで与えられた組み合わせの総和であり得るものを列挙する"""
    enumerated_sums = []
    enumerated_sums_append = enumerated_sums.append
    for i in range(2 ** len(l)):
        summation = 0
        # 0 -> len(l)桁目まで見ていく
        for j in range(len(l)):
            # 順番に見ていってj桁目のビットがたってたら足す
            if (i >> j) & 1:
                summation += l[j]
        enumerated_sums_append(summation)
    return enumerated_sums


def quick_enumerated_summations(l):
    """lで与えられた組み合わせの総和であり得るものを列挙する"""
    enumerated_sums = [sum(l[j] for j in range(len(l)) if (i >> j) & 1) for i in range(2 ** len(l))]
    return enumerated_sums


N, K = map(int, input().split())
A = list(map(int, input().split()))

enumerated_sum_first_half = quick_enumerated_summations(l=A[: (N // 2)])
enumerated_sum_last_half = quick_enumerated_summations(l=A[(N // 2) :])


# enumerated_sum_first_half.sort()
enumerated_sum_last_half.sort()

for first_piece in enumerated_sum_first_half:
    ans_cand_idx = bisect.bisect_left(enumerated_sum_last_half, K - first_piece)
    if ans_cand_idx < len(enumerated_sum_last_half) and first_piece + enumerated_sum_last_half[ans_cand_idx] == K:
        print("Yes")
        exit()

print("No")
