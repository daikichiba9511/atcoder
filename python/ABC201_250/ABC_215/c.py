import itertools
S, K = input().split()
K = int(K)

print("".join(sorted(set([i for i in itertools.permutations(S)]))[K - 1]))
