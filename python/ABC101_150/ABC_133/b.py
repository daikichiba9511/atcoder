import numpy as np
def main():
    n, d = map(int, input().split())
    x = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for i in range(n-1):
        for j in range(i+1, n):
            dist = np.linalg.norm(np.array(x[i]) - np.array(x[j])).item()
            if dist.is_integer():
                cnt += 1
    print(cnt)
if __name__ == "__main__":
    main()