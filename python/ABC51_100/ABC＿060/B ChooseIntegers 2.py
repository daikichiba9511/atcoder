

def main():
    # 状態がループする
    A, B, C = map(int, input().split())
    flag = False
    for i in range(1, B+1):
        if i * A % B == C:
            flag = True
    if flag:print("YES")
    else:print("NO")


if __name__ == "__main__":
    main()