from typing import List


def main()->None:
    l: List[int] = list(map(int, input().split()))
    l.sort()
    # 最大値l[2]からの差を考える。
    l[0] = l[2] - l[0]
    l[1] = l[2] - l[1]
    l[2] = 0
    
    # l[１]から見ていく
    count: int = 0
    while True:
        if l[1] - 2 < 0:
            if l[1] == 0:
                break
            else:
                l[1] -= 1
                l[0] -= 1
                count += 1
                break
        l[1] -= 2
        count += 1

    # l[0]について
    while True:
        if l[0] <= 0:
            if l[0] == 0:
                flag = True
                break
            if l[0] < 0:
                count += 1
                break
        l[0] -= 2
        count += 1
    print(count)


if __name__ == "__main__":
    main()