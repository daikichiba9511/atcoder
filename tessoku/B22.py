from __future__ import annotations

from typing import Container

INF = 10**64


def solve_dp(N: int, A: Container[int], B: Container[int]) -> None:
    """Solve the problem using dynamic programming.

    Args:
        N (int): The number of stairs.
        A (list): The cost of climbing one stair.
        B (list): The cost of climbing two stairs.

    Returns:
        int: The minimum cost to climb the stairs.
    """
    S = [INF] * N
    S[0] = 0
    for i in range(N - 1):
        S[i + 1] = min(S[i + 1], S[i] + A[i])
        if i == N - 2:
            continue
        S[i + 2] = min(S[i + 2], S[i] + B[i])
    return S[N - 1]


def test_solve_dp() -> None:
    """Test solve_dp."""
    """Case 1"""
    N = 3
    A = [10, 20, 30]
    B = [10, 20, 30]
    assert solve_dp(N, A, B) == 10

    """Case 2"""
    N = 5
    A = [30, 10, 60, 10, 60]
    B = [30, 20, 10, 50, 10]
    assert solve_dp(N, A, B) == 40


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(solve_dp(N, A, B))
