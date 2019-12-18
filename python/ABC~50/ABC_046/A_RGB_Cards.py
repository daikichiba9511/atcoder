

def main()->None:
    # 入力
    r:int, g:int, b:int = input().split(" ")
    num:int = int(r + g + b)
    if num % 4 == 0:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()