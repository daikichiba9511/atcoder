def main()->None:
    # sを昇順、tを皇潤に並べた後に比較すればいい
    # 解説見た
    s:str = input()
    s_asc:str = "".join(sorted(s))
    t:str = input()
    t_dasc:str = "".join(sorted(t, reverse=True))

    if s_asc < t_dasc: # ここなんでできるか正直ようわからん
        print("Yes")
    else:
        print("No")



if __name__ == "__main__":
    main()