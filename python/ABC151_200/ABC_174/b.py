def main():
    n , d = map(int, input().split())
    cordinate = 0
    for _ in range(n):
        x_i, y_i = map(int, input().split())
        ri = (x_i**2 + y_i**2)**(1/2)
        if ri <= d:
            cordinate += 1
    print(cordinate)

if __name__ == "__main__":
    main()