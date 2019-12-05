# 解説見た

def main()->None:
    # sを昇順、tを皇潤に並べた後に比較すればいい
    s = input()
    s＿asc = "".join(sorted(s))
    
    t = input()
    t_dasc = "".join(sorted(t, reverse=True))

    if s_asc < t_dasc: # ここなんでできるか正直ようわからん
        print("Yes")
    else:
        print("No")



if __name__ == "__main__":
    main()