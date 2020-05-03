
def f(x, a, b):
    return a * x // b - a * (x // b)

def main():
    a, b, n = map(int, input().split())
    return f(min(b-1, n), a, b)

if __name__ == "__main__":
    print(main())