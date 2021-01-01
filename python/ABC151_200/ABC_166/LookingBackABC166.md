# ABC166


## 感想
昨日に引き続き、安定の2完。しかも２ペケした。リストの初期化ミスと単純に$O(10 ^ 10)$全探索のを提出してた。。


## A. 

### 問題

### 制約

### 考察

### 解答

```python
def main():
    s = input()
    if s == "ABC":
        print("ARC")
    else:print("ABC")
if __name__ == "__main__":
    main()
```

## B. 

### 問題

### 制約

### 考察

### 解答

```python
def main():
    n, k = map(int, input().split())
    cnt = [0]*101
    for _ in range(k):
        d = int(input())
        A_i = list(map(int, input().split()))
        for i in range(1, n+1):
            if i not in A_i:
                cnt[i] += 1
    res = 0
    for j in cnt:
        if j == k:
            res += 1
    print(res)

if __name__ == "__main__":
    main()
```

## C. 

### 問題

### 制約

### 考察

### 解答

```python
def main1():
    # O(10 ^ 10)
    n, m = map(int, input().split())
    H = list(map(int, input().split()))
    p = [tuple(map(int, input().split())) for _ in range(m)]
    cnt = 0
    for i, h in enumerate(H):
        flag = True
        for a, b in p:
            if a != i and b != i:continue
            elif a == i:
                if h < H[b-1]:
                    flag = False
                    break
            elif b == i:
                if h < H[a-1]:
                    flag = False
                    break
        if flag:
            cnt += 1
    print(cnt)
```

## D. 

### 問題

### 制約

### 考察

### 解答

```python

```