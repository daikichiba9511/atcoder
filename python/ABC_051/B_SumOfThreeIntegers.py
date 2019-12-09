
def main()->None:
    K, S = map(int, input().split())

    range_x = range(K+1)
    range_y = range(K+1)

    counter = 0
    for x in range_x:
        for y in range_y:
            z = S - x - y
            if 0 <= z <= K:
                counter += 1
    print(counter)





if __name__ == "__main__":
    main()