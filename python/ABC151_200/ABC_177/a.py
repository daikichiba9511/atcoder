import sys

def main():
    input = sys.stdin.readline
    d, t, s = map(int, input().split(" "))

    if s * t < d:
        print("No")
    else:print("Yes")


if __name__ == "__main__":
    main()