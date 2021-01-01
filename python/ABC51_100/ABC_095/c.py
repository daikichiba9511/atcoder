def main():
    a, b, c, x, y = map(int, input().split())
    res = 10**100
    for i in range(10**5+1):
        pizza_a = max(0, x-i) * a
        pizza_b = max(0, y-i) * b
        pizza_c = 2 * c * i
        cost = pizza_c + pizza_a + pizza_b
        res = min(res, cost)
    print(res)

if __name__ == "__main__":
    main()